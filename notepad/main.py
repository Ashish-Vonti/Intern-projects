from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import time

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    statvar.set("Opening...")
    stat.update()
    time.sleep(2)
    statvar.set("Ready")
    stat.update()

    file = askopenfilename(defaultextension = ".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)

        f = open(file, "r")
        TextArea.insert(1.0,f.read())

        f.close()

def saveFile():
    global file
    statvar.set("Saving...")
    stat.update()
    time.sleep(2)
    statvar.set("Ready")
    stat.update()
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            #Save it as a New File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
    statvar.set("Cut...")
    stat.update()
    time.sleep(2)
    statvar.set("Ready")
    stat.update()

def copy():
    TextArea.event_generate(("<<Copy>>"))
    statvar.set("Copying...")
    stat.update()
    time.sleep(2)
    statvar.set("Ready")
    stat.update()
    

def paste():
    TextArea.event_generate(("<<Paste>>"))
    statvar.set("Pasting...")
    stat.update()
    time.sleep(2)
    statvar.set("Ready")
    stat.update()

def about():
    statvar.set("Busy")
    stat.update()
    time.sleep(1)
    statvar.set("Ready")
    stat.update()
    showinfo("Notepad", "Notepad by Me")

#Turning Night Mode On
def night_on():
    main_color = "#000000"
    second_color = "#373737"
    text_color = "green"
    root.config(bg = main_color)
    TextArea.config(bg=main_color, fg = "red")
    MenuBar.config(bg=main_color, fg = "red")
    FileMenu.config(bg=main_color, fg = "red")
    
#Turning Night Mode Off
def night_off():
    main_color = "white"
    second_color = "#373737"
    text_color = "black"
    root.config(bg = main_color)
    TextArea.config(bg=main_color, fg = "black")
    MenuBar.config(bg=main_color, fg = "black")
    FileMenu.config(bg=main_color, fg = "black")


if __name__ == '__main__':
    #Basic Tkinter Setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("C:\\Users\\cprit\\Desktop\\News_gui\\whack_notepad.ico")
    root.geometry("644x788")

    TextArea = Text(root, font = "lucida 13")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    #Creating a Menu Bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff = 0)

    #To open a New File
    FileMenu.add_command(label = "New", command = newFile)

    #To open already existing File
    FileMenu.add_command(label = "Open", command = openFile)

    #To save the current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)

    MenuBar.add_cascade(label = "File", menu = FileMenu)

    root.config(menu = MenuBar)

    #Adding Scrollbar using rules from tkinter
    scroll = Scrollbar(TextArea)
    scroll.pack(side = RIGHT, fill = Y)
    scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)



    #Edit Menu
    EditMenu = Menu(MenuBar, tearoff = 0)
    #To give a feature of Cut, Copy, Paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label = "Edit", menu = EditMenu)


    #Options Menu
    OptionsMenu = Menu(MenuBar, tearoff = 0)
    #To give a feature of Cut, Copy, Paste
    OptionsMenu.add_command(label = "Night Mode-ON", command = night_on)
    OptionsMenu.add_command(label = "Night Mode-OFF", command = night_off)

    MenuBar.add_cascade(label = "Options", menu = OptionsMenu)

    #Help Menu
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)

    MenuBar.add_cascade(label = "Help", menu = HelpMenu)

    statvar = StringVar()
    statvar.set("Ready")

    stat = Label(root,textvariable = statvar,relief=SUNKEN,anchor="w")
    stat.pack(side=BOTTOM,fill=X)


    root.mainloop()
