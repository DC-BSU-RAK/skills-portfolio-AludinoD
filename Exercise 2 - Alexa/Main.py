# Assessment 2
# Alexa Tell Me A Joke
# The theme of this app will be similar to the color scheme of Alexa which is Blue
# By : Deniz Marc Andrei Aludino
# Notes : 
# Some of the codes from Exercise 1 will be reused in this code(Mainly Frames, Images, Music, Sound Effects, and Maybe Layout.)
# Same Directory Issues, so make sure all the Assets are Downloaded.(Preferably if the whole Repository was downloaded/Cloned so its easier.)
# Requirements : 
# Pillow and PyGame are needed to run this. pip3 install pillow/PyGame in the terminal.
# GUI is also made in Figma so its easier to visualize.
# Canvas will be used again.

# Frame Flow
# Menu Screen -> Start Button -> Joke Screen -> Joke Button -> Exit Button
# Exit Button -> Exit Program


from tkinter import * # Main Tkinter Program
from PIL import Image, ImageTk # Images
import random # Random Jokes
import pygame # Sound Effects


# Main Window Setups
root = Tk()
root.title ("Alexa Tell Me A Joke")
root.geometry("500x500")
root.iconbitmap("alexaLogo.ico")  # Changed Window Icon

canvas = Canvas(root, width=500, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load Images

# Background Image that will be used for all screens
menuBg = Image.open("menuBg.jpg").resize((500,500))
bgImg = ImageTk.PhotoImage(menuBg)

# Alexa Figure
figure = Image.open("alexa.png")
figureImg = ImageTk.PhotoImage(figure)

def buttonStyle(text,command):
    btn = Button(root, text=text,font=("Arial", 12), width=10,command=command, bg="#007AFF", fg="#000000", activebackground="#005FCC", cursor="hand2")

    btn.bind("<Enter>", lambda e: btn.config(bg="#005FCC"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#007AFF"))
    return btn


# Clears Everything on the Canvas(Removes the other contents so the screen doesn't bug)
def clearCanvas():
    canvas.delete("all")

# Display Screens (Menu, Instructions, Jokes)
def displayMenu():
    clearCanvas()
    # The bg is actually just alexa+ on the middle, but I wanted to Add The "Tell me a Joke On top"
    canvas.create_image(0, 0, image=bgImg,anchor="nw")
        
    # Creating the Title and Buttons
    canvas.create_text(230, 120, text="Tell Me A Joke", font=("Arial", 32, "bold"), fill="white")
    # Buttons are Horizontally Arranged
    canvas.create_window(120, 410, window=buttonStyle("Play", lambda:()))
    canvas.create_window(250, 410, window=buttonStyle("Instructions",lambda:displayInstructions()))
    canvas.create_window(380, 410, window=buttonStyle("Exit",root.destroy))



def displayInstructions():
    pass


def displayJokeScreen():
    pass

# Tools

def loadJokes():
    pass

def showJoke():
    pass

def showPunchLine():
    pass


displayMenu()
root.mainloop()