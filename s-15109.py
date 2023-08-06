#importing tkinter library
from tkinter import *
from tkinter.ttk import *#pretty
import tkinter as tk



####################################
window =Tk() #creating the main window
window.geometry("345x150")  #size of the main window
window.title("ABDUL FATHIR")   #title of the window
window.resizable(False,False)  #No resizable option
####################################



#framing total 7 frames
frame1=Frame(window)
frame1.pack()
frame2=Frame(window)
frame2.pack()
frame3=Frame(window)
frame3.pack()
frame4=Frame(window)
frame4.pack()
frame5=Frame(window)
frame5.pack()
frame6=Frame(window)
frame6.pack()
frame7=Frame(window)
frame7.pack()




#Top secret bar label
label_lindex = Label(frame1,anchor="center", width=100, foreground="black", background="#808000")#0fffff##FF00F
label_lindex.pack(side="left")

#Top secret bar function#
def topbar_in(x):
    label_lindex["background"]="#ff00ff"
    label_lindex.configure(text="S-15109")

def topbar_out(y):
    label_lindex["background"] = "#808000"
    label_lindex.configure(text = "")
#
#
label_lindex.bind("<Enter>",topbar_in)
label_lindex.bind("<Leave>",topbar_out)

entry=Entry(frame2, width=250, justify="right")
entry.pack(side="left")
##

def type(ltr):
    current_ltr= entry.get()
    entry.delete(0,END)
    entry.insert(0,current_ltr +ltr)

    
def reverse():
    my_name= entry.get()
    rev_str= "".join(reversed(my_name))
    entry.delete(0,END)
    entry.insert(0,rev_str)
##########################


#Buttons                     #########################    
but_1=Button(frame3, text="A", command=lambda:type("A"))
but_1.pack(side="left")
but_2=Button(frame3, text="B", command=lambda:type("B"))
but_2.pack(side="left") 
but_3=Button(frame3, text="D", command=lambda:type("D"))
but_3.pack(side="left")
but_4=Button(frame3, text="U", command=lambda:type("U"))
but_4.pack(side="left")
but_5=Button(frame4, text="L", command=lambda:type("L"))
but_5.pack(side="left")
but_6=Button(frame4, text="F", command=lambda:type("F"))
but_6.pack(side="left")
but_7=Button(frame4, text="T", command=lambda:type("T"))
but_7.pack(side="left")
but_8=Button(frame4, text="H", command=lambda:type("H"))
but_8.pack(side="left")
but_9=Button(frame5, text="I", command=lambda:type("I"))
but_9.pack(side="left")
but_10=Button(frame5, text="R", command=lambda:type("R"))
but_10.pack(side="left")
but_11=Button(frame5, text="space", command=lambda:type(" "))
but_11.pack(side="left")
but_12=Button(frame5, text="reverse", command=reverse)
but_12.pack(side="left")
######################



labl_name=Label(frame6, text=" ",anchor="center", width=250, foreground="black", background="#c0c0c0")
labl_name.pack(side="left")
def topbar_in(x):
    labl_name["background"]="#ffa500"
    labl_name.configure(text="ABDUL FATHIR")

def topbar_out(y):
    labl_name["background"] = "#c0c0c0"
    labl_name.configure(text = "")

labl_name.bind("<Enter>",topbar_in)
labl_name.bind("<Leave>",topbar_out)



lb3=Label(frame7, text="Select the display color: ", width=25, foreground="black",background="pink")
lb3.pack(side="left")
def change_red(w):
    entry["foreground"]="red"
def change_cyan(w):#
    entry["foreground"]="cyan"
def change_jasminepurple(w):
    entry["foreground"]="#a23bec"
def change_brightgold(w):
    entry["foreground"]="#fdd017"

    
lbR=Label(frame7, width=7, background="red")
lbR.pack(side="left")
lbC=Label(frame7, width=7, background="cyan")
lbC.pack(side="left")
lbJ=Label(frame7, width=7, background="#a23bec")
lbJ.pack(side="left")
lbG=Label(frame7, width=7, background="#fdd017")
lbG.pack(side="left")



lbR.bind("<Button-1>",change_red)
lbC.bind("<Button-1>",change_cyan)
lbJ.bind("<Button-1>",change_jasminepurple)
lbG.bind("<Button-1>",change_brightgold)





def right_click(R):
    entry["foreground"]="black"
    entry.configure(text= " ")




    
entry.bind("<Button-3>",right_click)    








    

window.mainloop()































































