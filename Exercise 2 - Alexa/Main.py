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
# Menu Screen -> Start Button -> Joke Screen -> Joke Button -> Show Joke -> Next Joke -> Repeat until Exit
# Exit Button -> Exit Program

# Joke Screen Flow
# Empty Joke -> Joke Button -> Show Joke -> Reveal Joke -> Punchline Button -> Show Punchline -> Next Joke Button -> Repeat


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

# Main Menu Background Screen
menuBg = Image.open("menuBg.jpg").resize((500,500))
bgImg = ImageTk.PhotoImage(menuBg)

# Background 2 for other Frames
bg2 = Image.open("bg2.jpg").resize((500,500))
bgImg2 = ImageTk.PhotoImage(bg2)


# Alexa Figure
figure = Image.open("alexa.png").resize((100,100))
figureImg = ImageTk.PhotoImage(figure)

# Load Sound Effects

pygame.mixer.init()
pygame.mixer.music.load("elevMusic.mp3")
pygame.mixer.music.play(-1)  # Play background music on loop

# Button Click SFX
def clickSfx():
    clickSound = pygame.mixer.Sound("ClickSfx.mp3")
    clickSound.play()


# Laughing Sound Effects 
# Choose a random laugh mp3.
# Initialize options for the random module to choose from.
laughOptions = [
    "laugh1.mp3",
    "laugh2.mp3",
    "laugh3.mp3"
]

def laughSfx():
    laugh = random.choice(laughOptions)
    laughSound = pygame.mixer.Sound(laugh)
    laughSound.play()

def boomSfx():
    boom = pygame.mixer.Sound("boom.mp3")
    boom.play()

# Button Styles
def buttonStyle(text,command):
    clickSfx()
    btn = Button(root, text=text,font=("Arial", 12), width=12,command=command, bg="#007AFF", fg="#000000", activebackground="#005FCC", cursor="hand2")

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
    canvas.create_window(120, 410, window=buttonStyle("Play", lambda:displayJokeScreen()))
    canvas.create_window(250, 410, window=buttonStyle("Instructions",lambda:displayInstructions()))
    canvas.create_window(380, 410, window=buttonStyle("Exit",root.destroy))



def displayInstructions():
    clearCanvas()
    canvas.create_image(0, 0, image=bgImg2,anchor="nw")

    # Instructions Text
    instructions = ("Welcome to Alexa's Jokes!\n\n"
                    "1. Choose Play to Start.\n"
                    "2. Press 'Tell me a Joke' to hear a joke\n"
                    "3. Press 'Show Punchline to reveal it.'\n"
                    "4. Press 'Next Joke' for another.\n"
                    "5. Press 'Exit' if you had enough fun.\n"
                    "6. ENJOY! and Try not to laugh too loud!")
    
    # Creating the Title and Text
    canvas.create_text(250, 100, text="Instructions", font=("Arial", 32, "bold"), fill="white")
    canvas.create_text(250, 200,text=instructions,font=("Arial", 12),justify="center",width=400,fill="white")
    canvas.create_window(250, 320, window=buttonStyle("Back", lambda: displayMenu()))



def displayJokeScreen():
    clearCanvas()
    # Set Bg
    canvas.create_image(0, 0, image=bgImg2,anchor="nw")

    # Alexa Model
    canvas.create_image(350, 70, image=figureImg,anchor="nw")

    # Buttons
    canvas.create_window(180, 350, window=buttonStyle("Next Joke",lambda:showJoke()))
    canvas.create_window(250, 420, window=buttonStyle("Exit", root.destroy))
    canvas.create_window(320, 350, window=buttonStyle("Show Punchline",lambda:showPunchLine()))


# This Function opens the file and gets the jokes From the txt file.
# It gets a line and removes all spaces using the strip.
# It then finds the "?" in the text, then splits the text after the "?" so it becomes 2 seperate values.
# It then stores those values in setup and punchline that will be used in the showJoke and showPunchLine Functions.
def loadJokes():
    jokes = []
    try:
        with open("randomJokes.txt") as file:
            for line in file:
                line = line.strip()
                if "?" in line:
                    setup,punchline = line.split("?",1)
                    jokes.append((setup + "?", punchline))
        return jokes
    except:
        return [("Jokes Not Found, Unfunny.")]

jokes = loadJokes()
currentJoke = None

# This function works when the Show Joke Button is pressed.
# It chooses a random choice in the txt file and it deletes previous texts(if there is), then loads in the new one.
def showJoke():
    global currentJoke

    currentJoke = random.choice(jokes)
    canvas.delete("setupText")
    canvas.delete("punchText")

    canvas.create_text(200,120,text=currentJoke[0],font=("Arial",16,"bold"),fill="white",width=250,tags="setupText")
    boomSfx()

# This Function works when the Show Punchline Button Is Pressed.
# It checks if the Joke is available or not. If there's no joke yet, it tells the user there isn't any.
# But when there is, it shows the punchline
def showPunchLine():
    if not currentJoke:
        canvas.create_text(250,200, text="No Joke Yet",font=("Arial",16),fill="white",width=200,tags="punchText")
        return
    
    canvas.delete("punchText")
    canvas.create_text(250,230, text=currentJoke[1],font=("Arial",16),fill="white",width=200,tags="punchText")
    laughSfx()

# Improvements :
# Layout can be changed in the Display Joke Screen.
# Music and Sfx
# Maybe an add joke Function if thats possible? So the user can add Jokes if they want in the txt file.
# Probably Python Text To Speech

# Start Program
displayMenu()
root.mainloop()