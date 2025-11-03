# Assessment 1 
# Math Quiz
# The GUI theme is inspired by the game Baldi's Basics in Education and Learning
# By: Deniz Marc Andrei Aludino


# Import Modules
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


# Main Window Setups
root = Tk()
root.title ("Baldi's Math Quiz")
root.geometry("500x500")

# Functions
def startQuiz(difficulty):
    pass  # Placeholder for the startQuiz function

def displayMenu():
    # Before making the display Menu in code, I designed it on Figma first so I can have a clear idea of how it would look like.
    

    # Load and Resize Background Image to match window size (500x500)
    image = Image.open("Background.png").resize((500, 500))
    bg_image = ImageTk.PhotoImage(image)
    
    # Used Canvas to set the background image without the widgets(Buttons Box) overlapping the background.
    # Transparent Labels/Buttons were not possible if I used the Tkinter Buttons(Cuz They had their own background color).
    # I couldn't manipulate the background color because my background image wasn't a solid color.
    canvas = Canvas(root, width=500, height=500)
    canvas.pack(fill="both", expand=True) 
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    canvas.bg_image = bg_image

    # Title and Buttons
    canvas.create_text(250, 100, text="Baldi's Math Quiz", font=("Arial", 32, "bold"), fill="white")
    canvas.create_window(250, 200, window=Button(root, text="Play", width=20,font=("Arial", 12), command=lambda: startQuiz()))
    canvas.create_window(250, 260, window=Button(root, text="Instructions", width=20,font=("Arial", 12), command=lambda: displayInstructions()))
    canvas.create_window(250, 320, window=Button(root, text="Exit", width=20,font=("Arial",12), command=root.destroy))

    # Baldi Figure on the Left Side
    figure = Image.open("Baldi.png")
    figure_image = ImageTk.PhotoImage(figure)
    canvas.create_image(70, 270, image=figure_image, anchor="center")  
    canvas.figure_image = figure_image

def displayInstructions():
    pass

displayMenu()
root.mainloop()