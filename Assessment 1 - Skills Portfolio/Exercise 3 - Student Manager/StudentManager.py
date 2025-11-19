# Assessment 3
# Student Manager
# The Theme of this app is inspired by BathSpa University.
# By : Deniz Marc Andrei Aludino
# Notes : 
# Codes from previous exercises will be used here again. Especially the one in the Alexa because of the file handling.

from tkinter import * # Main Tkinter Program
from PIL import Image, ImageTk # Images


# Main Window Setups
root = Tk()
root.title ("BSU Student Manager")
root.geometry("900x500")
root.iconbitmap("BSUlogo.ico")  # Changed Window Icon

canvas = Canvas(root, width=900, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)


# Load Images
# BSU Background
Bsubg = Image.open("BSUbg.png").resize((900,500))
bgImg = ImageTk.PhotoImage(Bsubg)


# Button Style
def buttonStyle(text,command):
    btn = Button(root, text=text,font=("Arial", 12), width=20,command=command, bg="#23314F", fg="#FFFFFF", activebackground="#005FCC", cursor="hand2")


    btn.bind("<Enter>", lambda e: btn.config(bg="#195598"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#23314F"))
    return btn

def clearCanvas():
    canvas.delete("all")

# Screens
def displayMenu():
    clearCanvas()
    # Bg
    canvas.create_image(0, 0, image=bgImg,anchor="nw")

    #Title
    canvas.create_text(450, 45, text="Student Manager", font=("Arial", 32, "bold"), fill="white")
    # Buttons
    canvas.create_window(150, 150, window=buttonStyle("View All Student Record",lambda:allStudent()))
    canvas.create_window(450, 150, window=buttonStyle("View A Student Record",lambda:studentRecord()))
    canvas.create_window(750, 150, window=buttonStyle("Show Highest Mark",lambda:highestMark()))
    canvas.create_window(150, 250, window=buttonStyle("Show Lowest Mark",lambda:lowestMark()))
    canvas.create_window(450, 250, window=buttonStyle("Sort Student Record",lambda:sortStudent()))
    canvas.create_window(750, 250, window=buttonStyle("Add Student Record",lambda:addRecord()))
    canvas.create_window(300, 350, window=buttonStyle("Delete Student Record",lambda:deleteRecord()))
    canvas.create_window(600, 350, window=buttonStyle("Update Student Record",lambda:updateRecord()))

# Functions
def allStudent():
    pass

def studentRecord():
    pass

def highestMark():
    pass

def lowestMark():
    pass

def sortStudent():
    pass

def addRecord():
    pass

def deleteRecord():
    pass

def updateRecord():
    pass

displayMenu()
root.mainloop()