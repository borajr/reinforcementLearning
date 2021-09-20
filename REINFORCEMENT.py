import numpy as np
import random
from v2GUI import Start
import copy
from v2GUI import heatmap
import matplotlib.pyplot as plt

# from GUIqlearning import Start

# environment = np.zeros((5,5))



# environment[2][2] = 1

# print(environment)

# act = 1 #1 up , 2 down, 3 left, 4 right

# if act == 1:
#     environment[2][2] = 0
#     environment[1][2] = 1
# elif act == 2:
#     environment[2][2] = 0
#     environment[3][2] = 1 
# elif act == 3:
#     environment[2][2] = 0
#     environment[2][1] = 1
# else:
#     environment[2][2] = 0
#     environment[2][3] = 1
    
# print("*****************")
# print(environment)

#---------------------------------------------------------------
#---------------------------------------------------------------

# environment = np.zeros((5,5))

# x = random.randint(0, 4)
# y = random.randint(0, 4)


# environment[x][y] = 1
# # print(environment)



# a = 2
# b = 1

# # agent = environment[a][b]



# while environment[a][b] != 1:
#     act = random.randint(1, 4) #1 up 2 down 3 left 4 right
#     if act == 1 and a != 0:
#         a = a - 1
#     elif act ==2 and a !=4:
#         a = a + 1 
#     elif act ==3 and b != 0:
#         b = b - 1
#     elif act ==4 and b != 4:
#         b = b + 1
#     print("action is: " + str(act), end=" ")
#     print("a value is: "+ str(a), end=" ")
#     print("b value is: "+str(b))
    
    
    
# print(environment)  
    

#--------------------------------------------------------------

environment = np.zeros((5,5)) 

finalX = 3        
finalY = 2     

heatMap = np.zeros((25))

environment[finalX][finalY] = 1

#25 0 lı matristen heat map için en çok ziyaret edilen stateleri al
#en çok ziyaret edilen statelerin üstüne radius u daha büyük yuvarlak koy
#fade özelliği kullanılabilir heat mapte background renkleri değiştirilebilir

qTable = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
          [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
          [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
          [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
          [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

startStateX = 0
startStateY = 0 


reward = None

learningRate = 0.1

discountFactor = 0.95 #bir sonraki state e olan bağ

action = None

nextStateX = None
nextStateY = None

epsilon = 0.3



def maxQ(state):
    shuf = np.array(range(len(qTable[state])))
    random.shuffle(shuf)
    maxq = qTable[state][0]
    for k in shuf:
        if qTable[state][k] > maxq:
            maxq =  qTable[state][k]
    return maxq
        
        
        

def maxQindex(state):
    shuf = np.array(range(len(qTable[state])))
    random.shuffle(shuf)
    maxq = qTable[state][shuf[0]]
    maxqindex = shuf[0]
    for k in shuf:
        if qTable[state][k] > maxq:
            maxq =  qTable[state][k]
            maxqindex = k
    return maxqindex


def actionF(state):
    r = random.randint(1,100000)
    if r > epsilon * 100000:
        return maxQindex(state) + 1
    else:
        print("Explorative action") 
        return random.randint(1,4)
    
minseq = []  
lenseq = []
firstSeq = []
#1 up 2 down 3 left 4 right

for i in range(200):
    reward = 0
    currentStateX = startStateX
    currentStateY = startStateY
    nextStateX = currentStateX    #1 up 2 down 3 left 4 right
    nextStateY = currentStateY    #1 up 2 down 3 left 4 right
    seq = []
    while True:
        action = actionF(currentStateX*5 +currentStateY)
        if action == 1 and currentStateX != 0:
            nextStateX = currentStateX - 1
        if action == 2 and currentStateX != 4:
            nextStateX = currentStateX + 1
        if action == 3 and currentStateY != 0:
            nextStateY = currentStateY - 1
        if action == 4 and currentStateY != 4:
            nextStateY = currentStateY + 1
        
        seq.append(action) #appends the actions to sequence array
        
        if nextStateX == finalX and nextStateY == finalY:
            reward = 100
        else:
            reward = 0

        print(action, end=" ")
        print("Next state: " + str(nextStateX), end = " ")
        print(nextStateY, end = " ")
        print("reward = "+ str(reward))
        qTable[currentStateX*5 + currentStateY][action-1] = qTable[currentStateX * 5 + currentStateY][action-1] + learningRate * (reward + discountFactor * maxQ(nextStateX * 5 + nextStateY) - qTable[currentStateX * 5 + currentStateY][action-1])
        heatMap[currentStateX*5 + currentStateY] += 1
        
        currentStateX = nextStateX
        currentStateY = nextStateY
    
        
        if currentStateX ==finalX and nextStateY ==finalY:
            if epsilon > 0.01:
                epsilon = epsilon - 0.005
            break      
    if len(seq) < len(minseq) or i == 0:
        minseq = copy.deepcopy(seq)
    lenseq.append(len(seq))
    firstSeq.append(copy.deepcopy(seq))
for j in range(len(qTable)):
    print(maxQindex(j), end = " ")        
    if j % 5 == 4:
        print(" ")




print(environment)
print(minseq)
print("Adım sayısı = "+ str(len(minseq)))

heatMap = np.array(heatMap)
heatMap = heatMap/np.max(heatMap)
heatMap = np.power(np.e, heatMap - 1.12) # heat map değerlerini exponential olarak büyütüyoruz


for j in range(len(qTable)):
    print(heatMap[j], end = " ")        
    if j % 5 == 4:
        print(" ")
        

lenseq = np.array(lenseq)




a = []
a.append(minseq)

Start(startStateX, startStateY, finalY, finalX,200,"Öğrenme Öncesi - Q learning", firstSeq) #oyunun ilk episode u
Start(startStateX, startStateY, finalY, finalX,1000,"Öğrenme Sonrası - Q learning", a) # optimal yolu 


a = []
b = []

for j in range(len(qTable)):
    a.append(maxQ(j)) 

for i in range(len(lenseq)):
    if i > 20:
        b.append(np.average(lenseq[i - 20: i + 1]))
    else:
        b.append(np.average(lenseq[0:i + 1]))

print(" ")
print(b)




a = np.array(a)
a = a/np.max(a)


heatmap(a, finalY, finalX)

figure = plt.figure()
plt.plot(range(len(b)), b)
plt.title("Öğrenme Grafiği")
plt.xlabel("Episode sayısı")
plt.ylabel("Ortalama sequence uzunlukları")
plt.show()









