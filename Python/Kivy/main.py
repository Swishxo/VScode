#pay attention to kivy import patterns

import kivy
from kivy.app import App #builds the window
from kivy.uix.label import Label #builds labels
from kivy.uix.gridlayout import GridLayout #builds Gridlayout
from kivy.uix.textinput import TextInput #builds TextInput
from kivy.uix.button import Button #builds Button

#created class to hold design of application'
class MyGrid(GridLayout):
    def __init__(self, **kwargs): # **kwargs, allow you to take an unknown amount of args
        super(MyGrid, self).__init__(**kwargs) #pass class as args for super() as inheritance
        self.cols = 1 #how many spaces the button will take, also button  has its own 'cols' space

        self.inside = GridLayout() #inside get instance of GridLayout(), for TextInput()
        self.inside.cols = 2 #TextInput() spans two 'cols', left and right side

        #firstName
        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        #lastName
        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)
        #email
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        #add inside-GridLayout() to class-GridLayout
        self.add_widget(self.inside)

        #submit-Button() is the only instance belonging to class-GridLayout, it takes entire space
        self.submit = Button(text="submit", font_size = 24)
        #bind submit-Button() to function 'pressed' 
        self.submit.bind(on_press=self.pressed)
        #add submit-Button to widget
        self.add_widget(self.submit)

    #function created to bind to submit-Button()
    def pressed(self, instance):
        #pass TextInput() to vars
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        #display vars
        print("First Name: " + name + " Last Name: " + last + " Email: " + email)
        #when user hits submit-Button(), TextInput() is cleared
        self.name.text = " "
        self.lastName.text = " "
        self.email.text = " "
        


class MyApp(App):#inherit from kivy-App to use functionality

    def build(self): #is the main interface, use for initilization of application
        return MyGrid() #points to class MyGrid() 

#starts the program
if __name__ == "__main__":
    MyApp().run()
  
  
 
  
