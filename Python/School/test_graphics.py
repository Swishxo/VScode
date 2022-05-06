###
### http://anh.cs.luc.edu/handsonPythonTutorial/index.html
###

###
### http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
###

from random import triangular
from graphics import *

### Instantiate Graphics Window
win = GraphWin('my window', 1000,1000)

#change background of window
win.setBackground("black")

### Start your nested loops here

for x in range(10):

    for y in range(15):

        ### First pick a center point for the circle
        pt = Point(30 + 100 * x/2, y * 50)

        # Then draw the circle
        #cir = Circle(pt, 25)
        aRectangle = Rectangle(Point(30,40), Point(240,170))

        # Set the color
        #cir.setOutline('red')
        #cir.setFill('blue')
        aRectangle.setOutline('blue')
        aRectangle.setFill(color_rgb(110, 29, 130))
        
        message = Text(Point(100,100), "Welcome")
        message.setTextColor("white")
        message.setFace("arial")

        # Then render
        #cir.draw(win)
        aRectangle.draw(win)
        message.draw(win)
        

### end your loop here

# Wait for a mouse click to close the Graphics window
win.getMouse()
