# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random
from tkinter import messagebox

# from xml.etree.ElementTree import tostring

from numpy import size
 
# creating window using tkinter
Kartikey = Tk()
 
# the size of the window is defined
Kartikey.geometry("1200x700")
backg = Canvas(Kartikey)
Search = Frame(backg,bg = "Grey12")
bg = PhotoImage(file=r"E:\CSE N\PYTHON\Typing_Test\Home.png")
 
x = 0
 
# defining the function for the test
def game():
    global x
 
    # loop for destroying the window
    # after on test
    if x == 0:
        Kartikey.destroy()
        x = x + 1
 
    # defining function for results of test
    def check_result():
        if entry.get() == words[word]:
 
            # here start time is when the window
            # is opened and end time is when
            # window is destroyed
            end = timer()
 
            # we deduct the start time from end
            # time and calculate results using
            # timeit function
            Label(KK,text="Speed - ",font=30).place(x=390,y=400)
            Label(KK,text=end-start,font=30).place(x=450,y=400)
        else:
            messagebox.showerror("Error","Wrong Input.... You should type correctly.")
 
    words = ['Hello there! How are you doing today. I hope that you all have a very great day. Today is 20th July, 2022 and my birthday. Hope you all will enjoy this project.'
            ,'As I am not a hardcore coder.There may contain some mistakes or flaws within the project and you can tune it further and tell me in my instagram - @kartikay_jadli1601.'
            ,'In this project, we will develop a typing test that will help in improving your speed and accuracy.'
            ,'The user will be given 60 seconds and the user has to write as many words as possible that are displayed on the screen within the given time frame.'
            ,'Have you played a typing speed game? It’s a very useful game to track your typing speed and improve it with regular practice.'
            ,'Now, you will be able to build your own typing speed game in Python by just following a few steps.''']
 
    # Give random words for testing the speed of user
    word = random.randint(0, (len(words)-1))
 
    # start timer using timeit function
    start = timer()
    
    KK = Tk()
    KK.geometry("1000x1000")
    
    backg1 = Canvas(KK)
    Frame(backg1,bg = "Grey12")
    img = PhotoImage(file=r"E:\CSE N\PYTHON\Typing_Test\Page2.png")
    
    Label(KK, text="------TYPING TEST BY PYTHON------", font='san-serif 30 bold').pack()
    Label(KK, text="Instruction is to write the sentence in the Box.", font='san-serif 30 bold').place(x=350, y=55)
    # use label method of tkinter for labeling in window
    x2 = Label(KK, text=words[word], font='san-serif 12 bold')
 
    # place of labeling in window
    x2.place(x=180, y=200)
    x3 = Label(KK, text="Start Typing", font='san-serif 15 bold')
    x3.place(x=10, y=245)
 
    entry = Entry(KK,width=150,font=25)
    entry.place(x=150, y=250)
 
    # buttons to submit output and check results
    b2 = Button(KK, text="Done",command=check_result, width=20,font=25, bg='grey')
    b2.place(x=450, y=300)
 
    # b3 = Button(KK, text="Try Again",command=game, width=20,font=25, bg='grey')
    # b3.place(x=700, y=300)
    
    backg1.create_image(0,0,image = img,anchor=NW)
    backg1.pack(fill="both",expand = True)
    backg1.config(bg = "GREY12")
    KK.mainloop() 
 
x1 = Label(Kartikey, text="Lets start playing.. To Check Your Typing Speed", font="times 45")
x1.place(x=10, y=0)
 
b1 = Button(Kartikey, text="Go ->", command=game,font='san-serif 20 bold', bg='white',border=10)
b1.place(x=150, y=100)

backg.create_image(0,0,image = bg,anchor=NW)
backg.pack(fill="both",expand = True)
backg.config(bg = "GREY12")
 
# calling window
Kartikey.mainloop()