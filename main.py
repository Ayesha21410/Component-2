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

        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="#fca8f9", command=self.name_collection)
        self.continue_button.place(x=268,y=360)

    def name_collection(self):
        name=self.entry_box.get()
        if name == '':
            messagebox.showerror('Name is Vital!!!',
                                 'Please enter your name')
        elif len(name) > 20:

                          

            messagebox.showerror('limit error!!!',
                                 'please enter a name between 1 and 20 characters'
                                 )
        elif name.isnumeric():
            messagebox.showerror('Name error!!!',
                                 'Name can only consist of letters'
                                 )
        elif  not name.isalpha():
                messagebox.showerror('Name error!!',
                'name can not consist of symbols')
        else:
            names_list.append(name)  # add name to names list declared at the beginning
            self.entry_box.destroy()
            self.user_label.destroy()
            self.heading_label.destroy()
            self.continue_button.destroy()
            Instructionwindow(root)

#component 2 
class Instructionwindow:
    def __init__(self, parent):
            
            #background colour selection
            background_color2 = "#f7bfbe"
            background_color3= "#c7dfac"

             # code for bg image
            self.bg_img = Image.open('Quiz.png')  # update my image file
            image = ImageTk.PhotoImage(self.bg_img)  # update PhotoImage
            image_label= Label(root, image=bg_image)
            image_label.place(x=0, y=0, relwidth=1, relheight=1)
           
            # code for title image
            self.title_image = Image.open("Title.png") #need to use Image if need to resize 
            self.title_image = self.title_image.resize((295, 135), Image.ANTIALIAS)
            self.title_image = ImageTk.PhotoImage(self.title_image)
        
            self.heading_label=Label(parent, image=self.title_image, border=0)
            self.heading_label.place(x=170, y=110)

            # label for instruction 
            self.font_label=Label(parent,text="Do you want to read instruction?  ", font=("Tw Cen MT","14","bold"),bg=background_color3 )
            self.font_label.place(x=120, y=280)

            #Yes button
            self.yes_button = Button(parent, text="Yes,I want.", font=("Helvetica", "15", "bold"), bg="lightBlue",command=self.printinstruction)
            self.yes_button.place(x=125,y=362)
            #Skip button
            self.skip_button = Button(parent, text="No,Skip it.", font=("Helvetica", "15", "bold"), bg="Pink")
            self.skip_button.place(x=345,y=362)

        