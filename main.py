#Imports
from tkinter import *  
from PIL import Image, ImageTk # for Images
from tkinter import messagebox  # for error messages
import random
names_list = [] 
#Component 1
class QuizStarter:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
        background_color1="#f0dff2"
        background_color="#a3e4fa"
      
        #For title image
        self.title_image = Image.open("Title.png") #need to use Image if need to resize 
        self.title_image = self.title_image.resize((295, 135), Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(self.title_image)
        
        self.heading_label=Label(parent, image=self.title_image, border=0)
        self.heading_label.place(x=170, y=110) 

    
        #label for username
        self.user_label=Label(parent, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.place(x=120, y=260) 

         #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=230, y=320)

        