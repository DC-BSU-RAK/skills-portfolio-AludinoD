# Assessment 1 
# Math Quiz
# The GUI theme is inspired by the game Baldi's Basics in Education and Learning
# By: Deniz Marc Andrei Aludino
# Notes: 
# For some reason, the images don't show unless they're outside the folder? So I had them outside the Math Quiz(Ex1) folder.
# Before making all the GUI in code, I designed it on Figma first so I can have a clear idea of how it would look like.
# Most Buttons and Texts are from Canvas instead of Tkinter Widgets so it doesn't overlap the background image.
# Tkinter widgets has their own background color which makes it hard to blend with the background image(Bg Image isn't a solid color).

# Frame Flow:
# Menu Screen -> Play Button -> Difficulty Selection -> Quiz Screen -> Results Screen
# Result Screen -> Play Again Button -> Difficulty Selection
# Menu Screen -> Instructions Button -> Menu Screen 
# Exit Button -> Closes Program


# Import Modules
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


# Main Window Setups
root = Tk()
root.title ("Baldi's Math Quiz")
root.geometry("500x500")

# Create Canvas For all The screens
# Used Canvas to set the background image without the widgets(Buttons Box) overlapping the background.
# Transparent Labels/Buttons were not possible if I used the Tkinter Buttons(Cuz They had their own background color).
# I couldn't manipulate the background color because my background image wasn't a solid color.

canvas = Canvas(root, width=500, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load Images

# Background Image that will be used for all screens
image = Image.open("Background.png").resize((500, 500))
bg_image = ImageTk.PhotoImage(image)

# Baldi Image
figure = Image.open("Baldi.png")
figure_image = ImageTk.PhotoImage(figure)


# Functions

# Clears Everything on the Canvas(Removes the other contents so the screen doesn't bug)
def clearCanvas():
    canvas.delete("all")

def startQuiz(difficulty):
    pass  # Placeholder for the startQuiz function


def displayMenu():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    
    # Creating the Title and Buttons
    canvas.create_text(250, 100, text="Baldi's Math Quiz", font=("Arial", 32, "bold"), fill="white")
    canvas.create_window(250, 200, window=Button(root, text="Play", width=20,font=("Arial", 12), command=lambda: startQuiz()))
    canvas.create_window(250, 260, window=Button(root, text="Instructions", width=20,font=("Arial", 12), command=lambda: displayInstructions()))
    canvas.create_window(250, 320, window=Button(root, text="Exit", width=20,font=("Arial",12), command=root.destroy))

    # Baldi Figure on the Left Side
    canvas.create_image(80, 260, image=figure_image, anchor="center")  


def displayInstructions():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Instructions Text
    instructions = ("Welcome to Baldi's Math Quiz!\n\n"
                    "1. Choose 'Play' to start the quiz.\n"
                    "2. Answer 10 math questions of varying difficulty.\n"
                    "3. Your score will be calculated based on correct answers.\n"
                    "4. At the end, you'll receive a grade based on your score.\n"
                    "Good luck and have fun learning with Baldi!")
    
    # Creating the Title and Text
    canvas.create_text(250, 100, text="Instructions", font=("Arial", 32, "bold"), fill="white")
    canvas.create_text(250, 250,text=instructions,font=("Arial", 14),justify="center",width=400,fill="white")
    canvas.create_window(250, 400, window=Button(root, text="Back", width=20,font=("Arial", 12), command=lambda: displayMenu()))


def displayResults():
    clearCanvas()
    canvas.create_image(0, 0, image=image, anchor="nw")
    
    canvas.create_text(250, 100, text="Test Finished!", font=("Arial", 32, "bold"), fill="white")
    canvas.create_text(250, 200, text=f"Your Score: {score}/100", font=("Arial", 24), fill="white")


    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    canvas.create_text(250, 260, text=f"grade: {grade}", font=("Arial", 24), fill="white")
    canvas.create_window(250, 200, window=Button(root, text="Play Again", width=20,font=("Arial", 12), command=lambda: startQuiz()))
    canvas.create_window(250, 320, window=Button(root, text="Exit", width=20,font=("Arial",12), command=root.destroy))

def checkAnswer(user_answer):
    pass


displayMenu()
root.mainloop()