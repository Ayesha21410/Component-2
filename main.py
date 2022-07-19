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
        self.user_label=Label(parent, text="Please enter your username below: ", font=("Tw Cen MT","14","bold"),fg="Black",bg=background_color,highlightbackground = '#FF00FF', highlightthickness = 3)
        self.user_label.place(x=115, y=260)  #placement 

         #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=230, y=320)

        #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="#fca8f9",activebackground = "#a3e4fa" ,command=self.name_collection)
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
      
            # code for bg image
            self.bg_img = Image.open('Quiz.png')  # update my image file
            image = ImageTk.PhotoImage(self.bg_img)  # update PhotoImage
            self.image_label2= Label(root, image=bg_image) 
            self.image_label2.place(x=0, y=0, relwidth=1, relheight=1)
      
            #code for title image
            self.title_image = Image.open("Title.png") #need to use Image if need to resize 
            self.title_image = self.title_image.resize((295, 135), Image.ANTIALIAS) 
            self.title_image = ImageTk.PhotoImage(self.title_image)
            #label for title image 
            self.heading_label=Label(parent, image=self.title_image, border=0,)
            self.heading_label.place(x=170, y=110)
            
            # for instruction font
            self.font_label=Label(parent,text="Do you want to read instruction?  ", font=("Tw Cen MT","13","bold"),bg= "pink",highlightbackground = '#96DED1', highlightthickness = 5)
            self.font_label.place(x=135, y=280) #placement
   
            #Yes button
            self.yes_button = Button(parent, text="Yes,I want.", font=("Helvetica", "15", "bold"), bg="lightBlue",command=self.printinstruction)
            self.yes_button.place(x=125,y=362)
            #Skip button
            self.skip_button = Button(parent, text="No,Skip it.", font=("Helvetica", "15", "bold"), bg="Pink",command=self.questions_collection)
            self.skip_button.place(x=345,y=362)
                            
      #function for continue button in instruction window
    def printinstruction(self): 
          #background colour selection
            background_color2 = "#f7bfbe"
      
            # code for bg image
            self.bg_img = Image.open('Quiz.png')  # update my image file
            image = ImageTk.PhotoImage(self.bg_img)  # update PhotoImage
            image_label= Label(root, image=bg_image)
            image_label.place(x=0, y=0, relwidth=1, relheight=1)
      
            # code for title image
            self.title_image = Image.open("Title.png") #need to use Image if need to resize 
            self.title_image = self.title_image.resize((285, 120), Image.ANTIALIAS)
            self.title_image = ImageTk.PhotoImage(self.title_image)
            self.heading_label=Label(image=self.title_image, border=0) # label for title image 
            self.heading_label.place(x=170, y=90) #placement
      
            # for instructions
            self.printinstruction_image = Image.open("Instruction.png") #need to use Image if need to resize 
            self.printinstruction_image = self.printinstruction_image.resize((355, 180), Image.ANTIALIAS)
            self.printinstruction_image = ImageTk.PhotoImage(self.printinstruction_image)
            #label for print instruction image 
            self.printinstrution_label=Label(image=self.printinstruction_image,border=0 )
            self.printinstrution_label.place(x=130, y=210) #placement
      
            #To destroy Instructionwindow window and go to Quiz
            def continue_to_questions():
              self.heading_label.destroy()
              self.printinstrution_label.destroy()
              self.continue_button.destroy()
              self.image_label2.destroy()
              image_label.destroy()
              root.destroy()
              self.open_Questionwindow()
       
            #continue button
            self.continue_button = Button( text="Continue", font=("Helvetica", "10", "bold"), bg="#fca8f9",command=continue_to_questions )
            self.continue_button.place(x=250,y=390) #placement

    #skip button command      
    def questions_collection(self): 
            self.heading_label.destroy()
            self.image_label2.destroy()    
            root.destroy()#destroy the original window
            root2 = Tk()#open a new window had to rename to root2 here as root is in this fuction
            root2.title("General Knowledge Quiz!!")
            root2.geometry("600x500")
            Questionwindow(root2)
      
    #continue button command 
    def open_Questionwindow(self):
            root = Tk()
            root.title("General Knowledge Quiz!!")
            root.geometry("600x500")
            Questionwindow(root)
      
#Randomiser function which shuffles the keys in the dictionary.      
def shuffle():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked: #If the question (key) wasn't asked, then append it to the list.
    asked.append(qnum)
  elif  qnum in asked: #If question (key) was already appended to list, then shuffle keys again.
    shuffle()
    
      
      

   #*******Program runs below: *******#

if __name__=="__main__":
    root = Tk()
    
    root.title("General Knowledge Quiz!!")
    root.geometry("600x500")
    bg_image = Image.open("Quiz.png") #need to use Image if need to resize 
    bg_image = bg_image.resize((600, 500), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    quizStarter_object = QuizStarter(root) #instantiation, making an instance of the class QuizStarter to create the frame with its widget, passing root as j 
    quiz_instance = QuizStarter(root)
    
    
    
    root.mainloop()#so the window doesnt dissappear


      