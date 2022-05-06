from tkinter import *
#entry widget: a textbox that accepts a single line of user input

#Submit Func
def submit():
    username =entry.get()
    print("Hello "+ username)
    #after submiting username deactivate entry box
    entry.config(state=DISABLED)

#Delete Func
def delete():
    entry.delete(0, END)#deletes all charaters from entry box starting at 0 to the END

#Backspace
def backspace():
    entry.delete(len(entry.get()) -1,END)

window = Tk()

#Entry Box
entry = Entry(window,
              font= ("Arial", 50),
              fg= "gray",
              bg= "black",
              show="*")#used for passwords: whatever you choose is displayed


#entry.insert(0, "Name?")#insert default text: first-args = position 0 is begining, second-args is text you want
entry.pack(side=LEFT) #position entrybox to the left

#Submit button
submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT) #position button on the right

#Delete button
delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

#Backspace
backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()