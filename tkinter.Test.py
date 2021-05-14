from tkinter import *
import random

top = Tk()
playlist = []
myRolls = []
dieType = []
rollTimes= 0

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
    clearWindow()
    Lmain = Label(top, text = "Block 5 GUI Projects")
    Lmain.grid(column = 0, row= 1) 
    B1main = Button(text= "Week 1", bg= "white", command = week1)
    B1main.grid(colum = 0, row= 2)
    B2main = Button(text= "Week 2", bg= "white", command = week2)
    B2main.grid(column= 0, row= 3)
    B3main = Button(text= "Week 3", bg= "white")
    B3main.grid(column= 0, row= 4)


def week1():
   clearWindow()
   def results():
       result = E1.get()
       playlist.appennd(result)
       E1.delele(0, END)
    
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

Bexit = Button(text= " Clear ", bg = "#00ff00", command= mainMenu)
Bexit.grid(column= 1, row= 3)


def week2():
    def rollDice():
        #update variable data
        dieType = E2Week2.get()
        rollTimes = E1Week2.get()
        #clear window AFTER updating variables
        clearWindow()
        #roll the dice
        for x in range (0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #build the result window)
        L4Week2 = Label(top, text= "Heres your rolls!")
        L4Week2.grid(column= 0, row= 1)

        L5Week2 = Label(top, text= "{}".format(myRolls))
        L5Week2.grid(column= 0, row= 2)
    
        B2Week2 = Button(text="Main Menu", bg= "yellow", commmand= mainMenu)
        
  
    clearWindow()
    B1Week2 = Button(text= "Roll em!", bg="yellow", command = rollDice)
    B1Week2.grid(column = 2, row=4)

    L1Week2 = Label(top, text= "Dice Roller App")
    L1Week2.grid(column= 2, row= 1)

    L2Week2 = Label(top, text= "# of Rolls")
    L2Week2.grid(column= 0, row= 2)

    L3Week2 = Label(top, text= "# of Sides")
    L3Week2.grid(column= 3, row= 2)

    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column= 0, row = 3)

    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column= 3, row = 3)
    

    


if __name__ == "__main__":
    mainMenu()
    top.mainloop()




