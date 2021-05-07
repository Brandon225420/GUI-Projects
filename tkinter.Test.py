from tkinter import *

top = Tk()
playlist = []

def results():
    result = E1.get()
    playlist.append(result)
    print(playlist)
    E1.delete(0, END)

def printlist():
    print(playlist)

def exportlist():
    with open('text.txt','w') as f:
        for item in list:
            f.write("%s/n" % item)


def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWIndow()
    Lmain = Label(top, text = "Block 5 GUI Projects")
    Lmain.grid(column = 0, row= 1) 
    B1main = Button(text= "Week 1", bg= "white")
    B1main.grid(colum = 0, row= 2)
    B2main = Button(text= "Week 2", bg= "white")
    B2main.grid(column= 0, row= 3)
    B3main = Button(text= "Week 3", bg= "white")
    B3main.grid(column= 0, row= 4) 
    
        


    
#This is a Label widget
L1 = Label(top, text="Plavlist Generator")
L1.grid(column= 0, row= 1)

#This is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)

#This is7 a Button widget
B1 = Button(text="  Enter  ", bg="white", command= results)
B1.grid(column= 1, row= 2)

B2 = Button(text="  Print ", bg="blue", command= printlist)
B2.grid(column= 2, row= 2)

B3 = Button(text = "Export List", bg = "#B4FFCD", command = exportlist)
B3.grid(column= 0, row= 3)

#Bexit = Button(text= " Clear ", bg = "#00ff00", command= clearWindow)
#Bexit.grid(column= 1, row= 3)
top.mainloop()




