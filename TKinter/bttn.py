from tkinter import *

#button: you click it, an action is performed 

count = 10

def click():
    global count
    while count > 0:
        print(count)
        count = count - 1
        if count == 1:
            break
    print(count)
    print("Lift off!")


window = Tk()

photo = PhotoImage(file='logo.png')

button = Button(window, #window is the master and must be first command
                text= "click me!", #set text of button
                command= click,  #command: is a call to function, do not add parentensis when calling function
                font=("Verdana", 30),
                fg='yellow',
                bg='black',
                activeforeground= 'yellow',
                activebackground='black',
                state=ACTIVE, #state: can activate or disable a button
                image= photo,
                compound="bottom")
button.pack()


window.mainloop()