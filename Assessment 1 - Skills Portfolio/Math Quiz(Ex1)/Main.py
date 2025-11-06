# Assessment 1 
# Math Quiz
# The GUI theme is inspired by the game Baldi's Basics in Education and Learning
# By: Deniz Marc Andrei Aludino
# Notes: 
# For some reason, the images don't show unless they're outside the folder? So I had them outside the Math Quiz(Ex1) folder.
# Make sure that the images are downloaded and are in a folder.
# Also, make sure you have the Pillow module installed to run this program. pip3 install Pillow in the terminal.
# Pygame module is also needed for the sound effects. pip3 install pygame in the terminal.
# Before making all the GUI in code, I designed it on Figma first so I can have a clear idea of how it would look like.
# Most Buttons and Texts are from Canvas instead of Tkinter Widgets so it doesn't overlap the background image.
# Tkinter widgets has their own background color which makes it hard to blend with the background image(Bg Image isn't a solid color).


# Frame Flow:
# Menu Screen -> Play Button -> Difficulty Screen -> Quiz Screen -> Results Screen
# Result Screen -> Play Again Button -> Difficulty Screen
# Menu Screen -> Instructions Button -> Menu Screen 
# Exit Button -> Closes Program


# Import Modules
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

# Main Window Setups
root = Tk()
root.title ("Baldi's Math Quiz")
root.geometry("500x500")
root.iconbitmap("icon.ico")  # Changed Window Icon

# Create Canvas For all The screens
# Used Canvas to set the background image without the widgets(Buttons Box) overlapping the background.
# Transparent Labels/Buttons were not possible if I used the Tkinter Buttons(Cuz They had their own background color).
# I couldn't manipulate the background color because my background image wasn't a solid color.
canvas = Canvas(root, width=500, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load Images

# Background Image that will be used for all screens
image = Image.open("Background.png").resize((500, 500))
bgImg = ImageTk.PhotoImage(image)

# Baldi Image
figure = Image.open("Baldi.png")
figureImg = ImageTk.PhotoImage(figure)

# Load Sound Effects
pygame.mixer.init()
pygame.mixer.music.load("bgMusic.mp3")
pygame.mixer.music.play(-1)  # Play background music on loop


# Set Global Variables that will be used throughout the program.
# Need to set all to 0 or empty strings to reset values when starting.
# The Global Syntax will be used inside functions to modify these variables.
score = 0
questionNumber = 1
attempt = 1
selectedDifficulty = ""
operator = ""
num1 = 0
num2 = 0

# Int and Operator Randomizer Function(RNG!!!)

def randomInt(difficulty):
    if difficulty == "Easy":
        return random.randint(1, 9) # 1 Digit
    elif difficulty == "Moderate":
        return random.randint(10, 99) # 2 Digits
    elif difficulty == "Advanced": # Goodluck Math Experts !  
        return random.randint(1000, 9999) # 4 Digits

def decideOperator():
    return random.choice(['+', '-']) # Random Operator, either Addition or Subtraction.

# Program Core Functions

# Clears Everything on the Canvas(Removes the other contents so the screen doesn't bug)
def clearCanvas():
    canvas.delete("all")


def displayMenu():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")
    
    # Creating the Title and Buttons
    canvas.create_text(250, 100, text="Baldi's Math Quiz", font=("Arial", 32, "bold"), fill="white")
    canvas.create_window(250, 200, window=Button(root, text="Play", width=20,font=("Arial", 12), command=lambda: displayDifficulty()))
    canvas.create_window(250, 260, window=Button(root, text="Instructions", width=20,font=("Arial", 12), command=lambda: displayInstructions()))
    canvas.create_window(250, 320, window=Button(root, text="Exit", width=20,font=("Arial",12), command=root.destroy))

    # Baldi Figure on the Left Side
    canvas.create_image(80, 260, image=figureImg, anchor="center")  

# Instructions Screen
def displayInstructions():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    # Instructions Text
    instructions = ("Welcome to Baldi's Math Quiz!\n\n"
                    "1. Choose 'Play' to start the quiz.\n"
                    "2. Answer 10 math questions of varying difficulty.\n"
                    "3. Your score will be calculated based on correct answers.\n"
                    "4. At the end, you'll receive a grade based on your score.\n"
                    "Good luck and have fun learning with Baldi!")
    
    # Creating the Title and Text
    canvas.create_text(250, 100, text="Instructions", font=("Arial", 32, "bold"), fill="white")
    canvas.create_text(250, 200,text=instructions,font=("Arial", 12),justify="center",width=400,fill="white")
    canvas.create_window(250, 320, window=Button(root, text="Back", width=20,font=("Arial", 12), command=lambda: displayMenu()))

# Difficulty Screen
def displayDifficulty():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    # Creating the Title and Buttons
    canvas.create_text(250, 100, text="Select Difficulty", font=("Arial", 32, "bold"), fill="white")

    # Difficulty Buttons
    canvas.create_window(250, 200, window=Button(root, text="Easy", width=20,font=("Arial", 12), command=lambda: startQuiz("Easy")))
    canvas.create_window(250, 260, window=Button(root, text="Moderate", width=20,font=("Arial", 12), command=lambda: startQuiz("Moderate")))
    canvas.create_window(250, 320, window=Button(root, text="Advanced", width=20,font=("Arial", 12), command=lambda: startQuiz("Advanced")))
    canvas.create_window(250, 380, window=Button(root, text="Back", width=20,font=("Arial", 12), command=lambda: displayMenu()))


# Quiz Core Functions

# Quiz Logic Explanation:


# Chooses the difficulty and starts the quiz, resetting all the variables.
def startQuiz(selectedDifficulty):
    global difficulty,score,questionNumber, attempt # Access the global variables
    difficulty = selectedDifficulty
    score = 0
    questionNumber = 1
    attempt = 1
    displayProblem()


# Displays the Math Questions on the screen, along with the question number, score, input box, and buttons.
def displayProblem():
    global num1, num2, operator, answer,score # Access global variables for the operation and problems.
    clearCanvas()
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operator = decideOperator()

    canvas.create_text(250, 50, text=f"Question {questionNumber}/10", font=("Arial", 24, "bold"), fill="white")
    canvas.create_text(250, 100, text=f"Score: {score}/100", font=("Arial", 12), fill="white")
    canvas.create_text(250, 150, text=f"{num1} {operator} {num2} =", font=("Arial", 24), fill="white")
    answer = Entry(root, font=("Arial", 12),justify="center", width=20)
    canvas.create_window(250, 200, window=answer)
    canvas.create_window(250, 250, window=Button(root, text="Submit", width=20,font=("Arial", 12), command=lambda: checkAnswer(answer.get())))
    answer.focus_set()
    canvas.create_window(250, 300, window=Button(root, text="Exit", width=20,font=("Arial",12), command=lambda: displayMenu()))
    root.bind('<Return>', lambda event: checkAnswer(answer.get())) 



def checkAnswer(answer):
    global score, questionNumber, attempt, operator, num1, num2

    # Input Validation, making sure the answer is an integer. (Update, I just realized, negative numbers aren't allowed as it only allows digits)
    # Might Try another Method instead.
    # Found another method to check if the input is a valid number including negative numbers.
    try:
        answer = int(answer)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    # Calculate Answer based on the operator and given numbers.
    if operator == '+':
        correctAnswer = num1 + num2
    else:
        correctAnswer = num1 - num2

    # Adding Scores
    # 10 Points for 1st Attempt
    # 5 points for 2nd Attempt
    # No points if both attempts are wrong.
    # Update: Working as intended now, I realized that messagebox needs 2 values in order to show up properly(It was just showing title before)
    # Also you get 3 chances now, because before it was only 2 attempts(It wasn't working as intended too because you're supposed to get 3 chances)
    if answer == correctAnswer:
        if attempt == 1:
            score += 10
            messagebox.showinfo("Correct!", "You earned 10 points.")
        elif attempt == 2:
            score += 5
            messagebox.showinfo("Correct!", "However, that was your 2nd Attempt. You earned 5 points.")
        else:
            messagebox.showinfo("Correct!", "However, That was your 3rd Attempt. No points awarded.")

        questionNumber += 1
        attempt = 1
        
    else:
        if attempt < 3:
            attempt += 1
            messagebox.showwarning("Incorrect!", f"Try Again! (Attempt {attempt - 1}/3).")
            return
        else:
            messagebox.showinfo("Wrong again!", f"The correct answer was {correctAnswer}.")
            questionNumber += 1
            attempt = 1    

    # Check if the quiz is over after 10 questions.
    if questionNumber > 10:
        displayResults()
    else:
        displayProblem()


def displayResults():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    # Title and Score    
    canvas.create_text(250, 100, text="Test Finished!", font=("Arial", 32, "bold"), fill="white")
    canvas.create_text(250, 180, text=f"Your Score: {score}/100", font=("Arial", 24), fill="white")

    # Grading System
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

    # Display Grade & Buttons
    canvas.create_text(250, 250, text=f"Grade: {grade}", font=("Arial", 24), fill="white")
    canvas.create_window(250, 330, window=Button(root, text="Play Again", width=20,font=("Arial", 12), command=lambda: displayDifficulty()))
    canvas.create_window(250, 380, window=Button(root, text="Exit", width=20,font=("Arial",12), command=root.destroy))

# Main Program Works Well and as Intended.

# Improvements
# The GUI can still be improved more with proper spacings and better assets.
# I think Bg music and SFX can be added ? Will Try to add that if I figure it out.
# Better Buttons
# Maybe more operators to make it challenging
# Keyboard Inputs so users can just press Enter. Update: Added Enter Key and Auto Focus in the input bar.



# Start Program
displayMenu()
root.mainloop()