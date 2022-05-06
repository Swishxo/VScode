from tkinter import *

def display():
    if(x.get() == 1):
        print("You agree")
    else:
        print("You disagree")

window = Tk()

x = IntVar() #inVar() returns a 1 or a 0

check_button = Checkbutton(window,
                           text="I agree",
                           variable= x, #tracks the current state of the checkbutton, is an IntVar, and 0 means cleared and 1 means set
                           onvalue= 1, #used to know if variable is toggled on
                           offvalue= 0, #used to know if variable is toggled off
                           command=display) 
check_button.pack()

window.mainloop()