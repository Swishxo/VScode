#import the file
from tkinter import *

#widget: a GUI element: buttons, textboxes, labels, images
#windows: serves as a container to hold or contain these wideget

#first we must create the window

window = Tk()#instantiate window
window.geometry("420x420") #set size of window, must be in quotes, also no spaces
window.title("Steph python gui") #set title of window

#covert logo to photoimage
icon = PhotoImage(file='logo.png') 
window.iconphoto(True, icon)#set icon to windown

#config function is used when you want to make changes to your window
window.config(background="#adc7e0")
window.mainloop() #place window on computer screen 


