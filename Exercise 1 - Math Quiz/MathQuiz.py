# Assessment 1 
# Math Quiz
# The GUI theme is inspired by the game Baldi's Basics in Education and Learning
# By: Deniz Marc Andrei Aludino
# Notes: 
# For some reason, the images don't show unless they're outside the folder? So I had them outside the Math Quiz(Ex1) folder.
# Make sure that the images are downloaded and are in a folder.
# Also, make sure you have the Pillow module installed to run this program. pip3 install Pillow in the terminal.
# Pygame module is also needed for the sound effects. pip3 install pygame in the terminal.
# Before making all the GUI in code, I designed a rough sketch on Figma first so I can have a clear idea of how it would look like.(Especially cuz it uses x and y for positions)
# Most Buttons and Texts are from Canvas(Also a part of tkinter) instead of Tkinter Widgets so it doesn't overlap the background image.
# Tkinter widgets has their own background color which makes it hard to blend with the background image(Bg Image isn't a solid color).


# Frame Flow:
# Menu Screen -> Play Button -> Difficulty Screen -> Quiz Screen -> Results Screen
# Result Screen -> Play Again Button -> Difficulty Screen
# Menu Screen -> Instructions Button -> Menu Screen 
# Exit Button -> Closes Program


# Import Modules
from tkinter import * # Tkinter 
from tkinter import messagebox # Message Box
from PIL import Image, ImageTk # Images
import random # Number and Operator
import pygame # Sound Effects

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
bgmVol = 0.5
sfxVol = 0.5
pygame.mixer.music.load("bgMusic.mp3")
pygame.mixer.music.play(-1)  # Play background music on loop
pygame.mixer.music.set_volume(bgmVol) # Set Volume

# Sound Effects 
# Call when Correct Answer is given.
def correctSFX():
    correctSound = pygame.mixer.Sound("CorSfx.mp3")
    correctSound.set_volume(sfxVol)
    correctSound.play()


# Call when Incorrect Answer is given.
def incSFX():
    incorrectSound = pygame.mixer.Sound("IncSfx.mp3")
    incorrectSound.set_volume(sfxVol)
    incorrectSound.play()

# Click Button Sound Effect
def clickSfx():
    clickSound = pygame.mixer.Sound("ClickSfx.mp3")
    clickSound.set_volume(sfxVol)
    clickSound.play()

# Button Style
# Yellow ish Theme
# Has hover effects and cursor
def buttonStyle(text,command):
    clickSfx()
    btn = Button(root, text=text,font=("Arial", 12), width=20,command=command, bg="#ffd966", fg="#000000", activebackground="#ffc107", cursor="hand2")

    btn.bind("<Enter>", lambda e: btn.config(bg="#ffc107"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#ffd966"))
    return btn


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

# Main Menu Screen 
def displayMenu():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")
    
    # Creating the Title and Buttons
    canvas.create_text(250, 100, text="Baldi's Math Quiz", font=("Arial", 32, "bold"), fill="white")
    canvas.create_window(250, 200, window=buttonStyle("Play", lambda: displayDifficulty()))
    canvas.create_window(250, 260, window=buttonStyle("Instructions",lambda: displayInstructions()))
    canvas.create_window(250, 320, window=buttonStyle("Exit",root.destroy))

    # Baldi Figure on the Left Side
    canvas.create_image(80, 260, image=figureImg, anchor="center")  

# Instructions Screen
def displayInstructions():
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")
    canvas.create_image(80, 320, image=figureImg, anchor="center")  

    # Instructions Text
    instructions = ("Welcome to Baldi's Math Quiz!\n\n"
                    "1. Choose 'Play' to start the quiz.\n"
                    "2. Answer 10 math questions of varying difficulty.\n"
                    "3. Your score will be calculated based on correct answers.\n"
                    "4. At the end, you'll receive a grade based on your score.\n"
                    "Good luck and have fun learning with Baldi!\n"
                    "Change Volume Using The Sliders Below")
    
    # Creating the Title and Text
    canvas.create_text(250, 50, text="Instructions", font=("Arial", 32, "bold"), fill="white")
    canvas.create_text(250, 150,text=instructions,font=("Arial", 12),justify="center",width=400,fill="white")
    canvas.create_window(250, 300, window=buttonStyle("Back", lambda: displayMenu()))

        # Volume sliders Function
    def changebgmVol(val):
        global bgmVol
        bgmVol = float(val)
        pygame.mixer.music.set_volume(bgmVol)

    def changesfxVol(val):
        global sfxVol
        sfxVol = float(val)

    # Create Sliders 
    bgmSlider = Scale(root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL,length=200, label="BGM Volume", command=changebgmVol)
    bgmSlider.set(bgmVol)

    sfxSlider = Scale(root, from_=0, to=1, resolution=0.01, orient=HORIZONTAL,length=200, label="SFX Volume", command=changesfxVol)
    sfxSlider.set(sfxVol)

    # Create Sliders button
    canvas.create_window(250, 360, window=bgmSlider)
    canvas.create_window(250, 420, window=sfxSlider)

# Difficulty Screen
def displayDifficulty():
    global userNameEntry
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    # Creating the Title and Buttons
    canvas.create_text(250, 50, text="Name:", font=("Arial", 16, "bold"), fill="white")

    # Add Name Input Box
    userNameEntry = Entry(root, font=("Arial", 12),justify="center", width=20)
    canvas.create_window(250, 80, window=userNameEntry)
    userNameEntry.focus_set() # Auto Highlights Input Box

    canvas.create_text(250, 135, text="Select Difficulty", font=("Arial", 32, "bold"), fill="white")

    # Difficulty Buttons
    canvas.create_window(250, 200, window=buttonStyle("Easy", lambda: startQuiz("Easy")))
    canvas.create_window(250, 260, window=buttonStyle("Moderate", lambda: startQuiz("Moderate")))
    canvas.create_window(250, 320, window=buttonStyle("Advanced", lambda: startQuiz("Advanced")))
    canvas.create_window(250, 380, window=buttonStyle("Back", lambda: displayMenu()))



# Quiz Logic Explanation:
# Since each part of the code uses frames, its easier to show it part by part.
# When the user presses the Play Button in the Menu screen, it calls the difficulty screen.
# Users can then choose the difficulty, which then calls the startQuiz function.
# The startQuiz Function sets all the variables to 0 or empty strings so it doesn't save last game's data.
# It then calls the displayProblem function that shows the questions.
# The question comes from the combination of randomInt and decideOperator functions.
# The randomInt function generates random numbers based on the selected difficulty.
# While the decideOperator function randomly chooses either addition or subtraction.
# It then returns those global variables to display the problem.
# Additionally, the program uses those values to create the correct answer.
# The correct answer is then saved in the correctAnswer variable inside the checkAnswer function.
# The user then inputs their answer in the input box. Then they can either press the Submit button or Enter key to submit their answer.
# The CheckAnswer function then checks if the answer is correct or not.
# If the answer is correct, it adds score based on the attempt number(1st, 2nd, or 3rd attempt).
# If the answer is incorrect, it increases the attempt number and prompts the user to try again.
# After 3 attempts, and the answer is still wrong, it shows the answer and gives 0 points then moves to the next.
# It checks if there are more than 10 Questions, if it its more than 10, it shows the results screen
# If it's not, it continues until it reaches more than 10.


# Quiz Core Functions

# Chooses the difficulty and starts the quiz, resetting all the variables.
def startQuiz(selectedDifficulty):
    global difficulty,score,questionNumber, attempt, userName # Access the global variables
    difficulty = selectedDifficulty
    score = 0
    questionNumber = 1
    attempt = 1
    userName = userNameEntry.get().strip()
    # Checks if the user didn't add a username, if they didn't, it defaults to Player.
    if userName == "":
        userName = "Player"
    displayProblem()


# Displays the Math Questions on the screen, along with the question number, score, input box, and buttons.
def displayProblem():
    global num1, num2, operator, answer,score # Access global variables for the operation and problems.
    clearCanvas()
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    # Gets the Values from the functions and stores it.
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operator = decideOperator()

    # Prints all of the stored values that it got.
    # Labels
    canvas.create_text(250, 50, text=f"Question {questionNumber}/10", font=("Arial", 24, "bold"), fill="white")
    canvas.create_text(250, 100, text=f"Score: {score}/100", font=("Arial", 12), fill="white")
    canvas.create_text(250, 150, text=f"{num1} {operator} {num2} =", font=("Arial", 24), fill="white")
    answer = Entry(root, font=("Arial", 12),justify="center", width=20)
    answer.focus_set() # Auto Highlights the user input box
    canvas.create_window(250, 200, window=answer)
    # Buttons
    canvas.create_window(250, 250, window=buttonStyle("Submit", lambda: checkAnswer(answer.get())))
    canvas.create_window(250, 300, window=buttonStyle("Exit", lambda: displayMenu()))
    root.bind('<Return>', lambda event: checkAnswer(answer.get())) # Can press enter to submit instead of clicking button.


# Checks user Answers
def checkAnswer(user_input):
    global score, questionNumber, attempt, operator, num1, num2

    # Input Validation that checks if the user input is the correct type (Integer)
    try:
        user_answer = int(user_input)
    except ValueError: # In some cases where the user adds strings, it catches that error and tells them to enter a number.
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        answer.delete(0, END) # Deletes the input
        answer.focus_set() # Highlight input box
        return

    # Calculate Answer based on the operator and given numbers.
    if operator == '+':
        correctAnswer = num1 + num2
    else:
        correctAnswer = num1 - num2

    # Adding Scores
    # 10 Points for 1st Attempt
    # 5 Points for 2nd Attempt
    # 0 Points for 3rd Attempt
    # No points if both attempts are wrong.
    if user_answer == correctAnswer:
        if attempt == 1:
            correctSFX()
            score += 10
            messagebox.showinfo("Correct!", "You earned 10 points.")
        elif attempt == 2:
            correctSFX()
            score += 5
            messagebox.showinfo("Correct!", "However, that was your 2nd Attempt. You earned 5 points.")
        else:
            correctSFX()
            messagebox.showinfo("Correct!", "However, That was your 3rd Attempt. No points awarded.")

        questionNumber += 1
        attempt = 1
    # Wrong Answers
    else:
        if attempt < 3:
            incSFX()
            attempt += 1
            messagebox.showwarning("Incorrect!", f"Try Again! (Attempt {attempt - 1}/3).")
            answer.delete(0, END)
            answer.focus_set()
            return
        else:
            incSFX()
            messagebox.showinfo("Wrong again!", f"The correct answer was {correctAnswer}.")
            questionNumber += 1
            attempt = 1    

    # Check if the number of question is above 10. If it is, It shows the results
    # If it isn't, it continues.
    if questionNumber > 10:
        displayResults()
    else:
        displayProblem()

# Results Screen
def displayResults():
    global userName # Grabs the userName so the program can call it.
    clearCanvas()
    # Set Background
    canvas.create_image(0, 0, image=bgImg, anchor="nw")

    # Title and Score    
    canvas.create_text(250, 100, text=f"Congrats {userName}! The test is Finished!", font=("Arial", 18, "bold"), fill="white")
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
    canvas.create_window(250, 330, window=buttonStyle("Play Again", lambda: displayDifficulty()))
    canvas.create_window(250, 380, window=buttonStyle("Exit", root.destroy))

# Final Version that works, until further updates.
# Current Features the quiz has :
# Different Screens for each part of the quiz.
# Button Hover Effects (Cursor and Color) and a style.
# Input Validations
# 2 random Operators (Addition & Subtraction)
# 3 Difficulty Levels that user can choose (Easy, Moderate, Advanced).
# Random Number Generator that's based on the users difficulty Level.
# Auto Highlights Input Boxes, and auto Deletes them after submission(so user doesn't need to delete manually).
# Binded Enter Key(So user doesn't need to press submit manually).
# Theres also messageboxes that tell if the user is correct or wrong.
# Result Screen at the end that : 
# Shows Grade and Total Points acquired.
# Play button or exit.

# Additionally, It also has Bg music, sound effects (Correct, Incorrect, Clicking button).
# And A Custom Icon for the game.

# Start Program
displayMenu()
root.mainloop()