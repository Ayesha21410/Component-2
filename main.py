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

#Question class that has all the quiz options and calculation methods.
class Questionwindow:
    def __init__(self,parent): 
            #bg colour selection
            background_color=  "#a3e4fa"
            background_color1= "#00FF00"
            background_color2 = "#f7bfbe"
            background_color3 = "#000000"
            background_color4 = "#7F00FF"
            background_color5=  "#C3B1E1"
            background_color6=  "#ff0000"
      
            
            #Dictionary that contains the keys and values of questions 1-10.
            self.questions_answers= {
  #Keys contain values that is the question and answers.
  1: [" What is the capital of Finland?" , "Sweden" , "Estonia." , "Norway." , "Helsinki." , "Helsinki." , 4],

  2: ["  What's the biggest animal in the world?" , "  The blue whale." , "African Elephant." , "Giraffe." , "Ostrich." , "The blue whale." , 1],

  3: ["Which country is brie cheese originally from?" , "China." , "America." , "France." , "Australia.", "france." , 3],

  4: ["What is the largest country in the world?" , "America." , "Russia." , "Cnada." , "Brazil.", "Russia." , 2],

  5: ["Who came second in the FIFA Women's World Cup in 2019?" , "England." , "Netherlands" , "France" , "Spain" , "Netherlands." , 2],

  6: ["Typically, what's the strongest muscle in the human body?" , "pectoral muscle." , "Tricep muscle." , "masseter muscle ." ,"biceps muscle", "masseter muscle." , 3],

  7: ["How many minutes in a game of rugby league?" , "80 minutes." , "60 minutes." , "20 minutes." ,"120 minutes" ,"80 minutes." , 1],

  8: ["Which planet is closest to the sun?" , "Mercury." , "Venus." , "Earth." , "Jupitar.", "Mercury." , 1],

  9: ["What fruit takes the scientific name Mangifera indica?" , "Orange.", "Banana." , "Mango.", "Apple." , "Mango." , 3],

  10: ["How many sides does a heptadecagon have?" , "Eighteen." , "Ten." , "Twenty." , "Seventeen." , "Seventeen." , 4],
}
            #frame set up
            self.quiz_frame = Frame(parent, 
        bg=background_color3)
            self.quiz_frame.pack(fill = "both", expand = True)
            
            # code for title image
            self.title_image = Image.open("Title2.png") #need to use Image if need to resize 
            self.title_image = self.title_image.resize((305, 140), Image.ANTIALIAS)
            self.title_image = ImageTk.PhotoImage(self.title_image)
            self.heading_label=Label(image=self.title_image, border=0)
            self.heading_label.place(x=145, y=20)
      
            #Question counter label.
            self.questioncounter_label = Label(self.quiz_frame , text = "QUESTION NUMBER : ", font = ("Helvetica", "11", "bold"), foreground = 'white', bg = background_color4, highlightbackground = '#CF9FFF', highlightthickness = 3, pady = 5) #Attributes.
            self.questioncounter_label.place(x = 170, y = 180) #Placement.

            #Question number calculated label.
            self.qnumber_label = Label(self.quiz_frame , text ="", font = ("Helvetica", "11", "bold"), bg = background_color4, foreground = 'white', highlightbackground = '#CF9FFF', highlightthickness = 3, pady = 5) #Attributes.
            self.qnumber_label.place(x = 368, y = 180) #Placement.
            
            shuffle() #Method to randomise the questions.

            #questions
            self.question_label=Label(self.quiz_frame , text= 
self.questions_answers[qnum][0], font=("Tw Cen MT","11","bold"),bg=background_color,justify = 'center',padx=10 ,wraplength = 480,highlightbackground = '#00008B', highlightthickness=3)
            self.question_label.place(x = 70, y = 240)  #placement 
      
            self.var1=IntVar()  #Holds the value of radio buttons.

            #option 1
            self.rb1 = Radiobutton (self.quiz_frame , text = self.questions_answers[qnum][1], font=("Helvetica", "10"), bg=background_color5, value=1, variable=self.var1, pady=5,padx=8,relief = RAISED, wraplength = 200,width = 17, indicatoron = 0, activebackground = "Pink")
            self.rb1.place(x = 10, y = 305) #placement 
            #option2
            self.rb2 = Radiobutton (self.quiz_frame , text = self.questions_answers[qnum][2], font=("Helvetica", "10"), bg=background_color5, value=2, variable=self.var1, pady=5,padx=8,relief = RAISED,width = 17,wraplength = 200, indicatoron = 0, activebackground = "Pink")
            self.rb2.place(x = 374, y = 305) #placement
            #option3
            self.rb3 = Radiobutton (self.quiz_frame , text = self.questions_answers[qnum][3], font=("Helvetica", "10"), bg=background_color5, value=3, variable=self.var1, pady=5,padx=8,relief = RAISED,width = 17,wraplength = 200, indicatoron = 0, activebackground = "Pink")
            self.rb3.place(x = 10, y = 360) #placement
            #option4
            self.rb4 = Radiobutton (self.quiz_frame , text = self.questions_answers[qnum][4], font=("Helvetica", "10"), bg=background_color5, value=4, variable=self.var1, pady=5,padx=8,relief = RAISED,width = 17,wraplength = 200, indicatoron = 0, activebackground = "Pink")
            self.rb4.place(x = 374, y = 360) #placement 
      
            
             
    
      
      

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


      