from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='logo.png')

#label constructor must contain the window as first args
label = Label(window,
              text= "Hello Steph", 
              font= ("Arial", 20, "bold"),
              fg= "gray",#fg: means foreground, and it changes the font color
              bg= "black",#bg: means background, and it changes the background of font color
              image = photo,#image: adds the photo to the widget
              compound='bottom')#compound: changes the direction of image

label.pack()#positions the Label on the main window


window.mainloop()

