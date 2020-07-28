from tkinter import *
root = Tk()
root.title("Calculator")
root.configure(background = "black")
root.geometry("400x900")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()    


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar = scvalue, font = "lucida 40 bold")
screen.pack(fill = X, pady = 10, padx = 10)

f = Frame(root, bg = "black")
b = Button(f, text = "C", padx = 2, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "%", padx = 50, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 10, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "/", padx = 10, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg = "black")
b = Button(f, text = "9", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "8", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "7", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "*", padx = 7, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "black")
b = Button(f, text = "6", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "5", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "4", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "+", padx = 3, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg = "black")
b = Button(f, text = "3", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)


b = Button(f, text = "2", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "1", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "-", padx = 7, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "black")
b = Button(f, text = "0", padx = 60, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 10, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = ".", padx = 10, pady = 10, font = "lucida 35 bold",bg="grey")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=", padx = 3, pady = 10, font = "lucida 35 bold",bg="orange",relief=FLAT)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()
root.mainloop()