import tkinter as tk
from tkinter import messagebox



def Start(startStateX, startStateY, finalX, finalY, time, name, episodes):
        
    global root 
    root = tk.Tk()
    
    
    
    root.title(name)
    
    root.geometry("400x480+300+200")
    
    
    framecolor = "lightgreen"
    
    cerceve = tk.Frame(root, bg = framecolor)
    cerceve.pack()
    cerceve.place(relwidth = 1, relheight = 1)
    
    
    a = cerceve
    
    w = 68
    h= 68
    x = w//3
    y = h//3
    
    
    
    vertical = 4
    horizontal = 4
    
    #episodun biteceği stateleri alıcak
    def destination(finalX, finalY):
        terminalState = tk.Canvas(root, width = w, height = h, bg = "purple")
        terminalState.grid(pady = vertical, padx = horizontal, row = finalY, column = finalX)
    
    # finalX = 2 #yFin() #ters bağlı y oynatmak için xde değişim olucak !!
    # finalY = 3 #xFin() #ters bağlı x oynatmak için yde değişim olucak
    
    
    def quitL():
        global root
        root.quit()
    
    
    
    
    
    def createWorld(agentX, agentY, time, episodeNum):
        for row in range(5):
            for column in range(5):
                canvas = tk.Canvas(root, bg = framecolor, height = 68, width = 68)
                canvas.grid(row = row, column = column, padx = 4, pady = 4)
                destination(finalX, finalY)
            createAgent = tk.Canvas(root, width = w, height = h, bg = "red")
            createAgent.grid(pady = vertical, padx = horizontal, row = agentY, column = agentX)
        table = tk.Canvas(root, bg = framecolor, height = 68, width = 68)
        table.grid(row = 5, column = 2, padx = 4, pady = 4)  
        table.create_text(34, 34, text = str(episodeNum), font = "Times 34")
        root.after(time, quitL)
        
        
     #startState #startX, startY ?
    
    
    
    
    # createAgent = tk.Canvas(root, width = w, height = h, bg = "red")
    # createAgent.grid(pady = vertical, padx = horizontal) #4er pad
    
    
    # circle = createCircle.create_oval(x, y, x + 26, y + 26)
    
    
    
    
    
    #call mainloop
    #loopun sonunda window.after zaman limiti ... sonra quit ve tekrar mainloop
    
    
    
    
    
    
    # act = [2, 2, 2, 2, 3, 3, 3, 1, 4]
    
    
    # agentxlist = []
    # agentylist = []
    num = [0, 3, 8, 12, 15, 20, 25, 30, 75, 90]
    if len(episodes) == 1:
        num = [0]        
    
    for i in num:
        seq = episodes[i]
        if len(episodes) == 1:
            i = 199
        createWorld(startStateX, startStateY, time, i + 1)
        root.mainloop()
        agentX = startStateY #startX 
        agentY = startStateX #startY 
        for action in seq:
        # for action in act:
            if action == 1 and agentY != 0:                                         #up
                agentY = agentY - 1
                
                   
            elif action == 2 and agentY != 4:                                       #down
                agentY = agentY + 1    
                
            
            elif action == 3 and agentX != 0:                                       #left
                agentX = agentX - 1
                
            elif action == 4 and agentX != 4:                                       #right
                agentX = agentX + 1
        
            
            createWorld(agentX, agentY, time, i + 1)
            root.mainloop()
        
    
    def winStatus():
        game_over = tk.Frame(root, borderwidth = 1, height = 500, width = 500)
        game_over.place(relx = 0.5, rely = 0.5, anchor = "center")
        tk.Label(game_over, text = "KAZANDINIZ!", bg = "thistle1", fg = "coral1", font = ("Arial",20)).pack()
    
            
    if agentX == finalX and agentY == finalY and len(episodes) == 1:    
        winStatus()
        # print("kazandınız!")
    
    
    
    
    
    
    # root.bind("<KeyPress-Left>", lambda event: BALL.left(event)) 
    # root.bind("<KeyPress-Right>", lambda event: BALL.right(event)) 
    # root.bind("<KeyPress-Up>", lambda event: BALL.up(event)) 
    # root.bind("<KeyPress-Down>", lambda event: BALL.down(event)) 





    root.mainloop()    
    
    
def heatmap(heatMap,finalX, finalY):
    window = tk.Tk()
    
    window.title("Heat Map")
    
    window.geometry("400x400")
    
    framecolor = "Orange"
    
    cerceve = tk.Frame(window, bg = framecolor)
    cerceve.pack()
    cerceve.place(relwidth = 1, relheight = 1)    
    
    w = 68
    h= 68
    x = w//3
    y = h//3
    
    
    
    vertical = 4
    horizontal = 4
    
    def destination(finalX, finalY):
        terminalState = tk.Canvas(window, width = w, height = h, bg = "lightblue")
        terminalState.grid(pady = vertical, padx = horizontal, row = finalY, column = finalX)
    
    
    def heatWorld(heatMap, finalX, finalY):
        for row in range(5):
            for column in range(5):
                canvas = tk.Canvas(window, bg = framecolor, height = 68 , width = 68)
                canvas.grid(row = row, column = column, padx = 4, pady = 4)
                createAgent = tk.Canvas(window, width = w * heatMap[row*5 + column],
                                        height = h * heatMap[5*row + column],
                                        bg = "red", highlightthickness = 0)
                createAgent.grid(pady = vertical, padx = horizontal, row = row, column = column)
        destination(finalX, finalY)
    
    
    
        
        
    
        
    heatWorld(heatMap, finalX, finalY)
    
    window.mainloop()
    
    


    

# Start()
