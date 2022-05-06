#radio button: similar to checkbox, but you can only select one from a group 

from tkinter import *

#Creat a list of food
food = ["Pizza", "Seafood", "Hotdog"]

#create window to display
window = Tk()

x = IntVar()

#for-loop to loop through food-list 
for i in range(len(food)):
    radio_button = Radiobutton(window, 
                               text=food[i], #each button is assigned text from food-list, i is used to index through the food list
                               variable=x, #groups radiobuttons together if they share the same variable
                               value=i, #assigns each radiobutton a different value
                               font= ("impact", 16) #changes font
                               ) 
    radio_button.pack(anchor=W) #organize each button within widget 

window.mainloop()