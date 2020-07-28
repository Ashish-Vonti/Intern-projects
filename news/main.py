from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
root = Tk() 
root.geometry("444x234") 
Scrollbar(root).pack(side=RIGHT,fill=Y)

def click():
    tmsg.showinfo("Succesfull.","Thank you for submitting your Email ID and for Rating us!!")

head = Label(text = "NewsLine", bg= "red", fg = "white", padx = 80, pady = 30, font = "comicsansms 19 bold", borderwidth = 10)
head.pack(fill=X) 

sub = Label(text = "Russia Launches a Destroyer", bg= "grey", fg = "white", padx = 80, pady = 30, font = "comicsansms 19 bold", borderwidth = 10)
sub.pack() 

f1 = Frame(root, borderwidth = 6, bg = "grey")
f1.pack(pady=10)

image = Image.open("rocket.jpg")
photo = ImageTk.PhotoImage(image)
mylabel1 = Label(f1,image = photo)
mylabel1.pack()

Label(f1,text="The U.S. government says Russia tested a space weapon earlier this month.").pack()
Label(f1,text=" Russia says the device, launched July 15, is not a weapon but rather a satellite designed to inspect other satellites.").pack()
Label(f1,text="But, the U.S. Space Command (USCC) said in a statement that the Russians launched an anti-satellite weapon.").pack()

Label(root,text="Enter your email id to get updates on latest news!!").pack()
mailid= StringVar()
Entry(root,textvariable=mailid).pack()
Label(root,text="Rate us!!").pack()
Scale(root, from_ = 0, to = 5, orient=HORIZONTAL).pack()
Button(root, text="Submit",command=click).pack()










root.mainloop()

