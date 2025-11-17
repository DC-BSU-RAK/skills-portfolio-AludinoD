# Assessment 2
# Alexa Tell Me A Joke
# The theme of this app will be similar to the color scheme of Alexa which is Blue
# By : Deniz Marc Andrei Aludino
# Notes : 
# Some of the codes from Exercise 1 will be reused in this code(Mainly Frames, Images, Music, Sound Effects, and Maybe Layout.)
# Same Directory Issues, so make sure all the Assets are Downloaded.(Preferably if the whole Repository was downloaded/Cloned so its easier.)
# GUI is also made in Figma so its easier to visualize.
# Canvas will be used again.

# Requirements : 
# Pillow and PyGame are needed to run this. pip3 install pillow/PyGame in the terminal.

# Frame Flow
# Menu Screen -> Start Button -> Joke Screen -> Joke Button -> Show Joke -> Next Joke -> Repeat until Exit
# Exit Button -> Exit Program

# Joke Screen Flow
# Empty Joke -> Joke Button -> Show Joke -> Reveal Joke -> Punchline Button -> Show Punchline -> Next Joke Button -> Repeat


from tkinter import * # Main Tkinter Program
from PIL import Image, ImageTk # Images
import random # Random Jokes & Random Laugh Option
import pygame # Sound Effects
import pyttsx3 # Text To Speech
import threading


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
# Initialize Sound Effects Volume
pygame.mixer.init()
bgmVol = 0.5
sfxVol = 0.5

# Bg Music
pygame.mixer.music.load("elevMusic.mp3")
pygame.mixer.music.play(-1)  # Play background music on loop
pygame.mixer.music.set_volume(bgmVol) # Set Volume


# Button Click SFX
def clickSfx():
    clickSound = pygame.mixer.Sound("ClickSfx.mp3")
    clickSound.set_volume(sfxVol)
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
    laughSound.set_volume(sfxVol)
    laughSound.play()

# Next Joke Sfx
def boomSfx():
    boom = pygame.mixer.Sound("boom.mp3")
    boom.set_volume(sfxVol)
    boom.play()

# Text To speech Engine
def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    threading.Thread(target=run, daemon=True).start()


# Button Styles
def buttonStyle(text,command):
    btn = Button(root, text=text,font=("Arial", 12), width=12,command=command, bg="#007AFF", fg="#000000", activebackground="#005FCC", cursor="hand2")
    clickSfx()

    btn.bind("<Enter>", lambda e: btn.config(bg="#005FCC"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#007AFF"))
    return btn


# Clears Everything on the Canvas(Removes the other contents so the screen doesn't bug)
def clearCanvas():
    canvas.delete("all")

# Display Screens (Menu, Instructions, Jokes)
# Main Menu Screen
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


# Instruction Screen
def displayInstructions():
    clearCanvas()
    # Bg
    canvas.create_image(0, 0, image=bgImg2,anchor="nw")

    # Instructions Text
    instructions = ("Welcome to Alexa's Jokes!\n\n"
                    "1. Choose Play to Start.\n"
                    "2. Press 'Next Joke' to hear a joke\n"
                    "3. Press 'Show Punchline to reveal it.'\n"
                    "4. Press 'Next Joke' for another.\n"
                    "5. Press 'Exit' if you had enough fun.\n"
                    "6. ENJOY! and Try not to laugh too loud!\n"
                    "Change Volume Using The Sliders Below.")
    
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



# Jokes Screen
def displayJokeScreen():
    clearCanvas()
    # Set Bg
    canvas.create_image(0, 0, image=bgImg2,anchor="nw")

    # Alexa Model
    canvas.create_image(350, 70, image=figureImg,anchor="nw")

    # Buttons
    canvas.create_window(180, 350, window=buttonStyle("Next Joke",lambda:showJoke()))
    canvas.create_window(250, 420, window=buttonStyle("Return", lambda:displayMenu()))
    canvas.create_window(320, 350, window=buttonStyle("Show Punchline",lambda:showPunchLine()))

# Tools Functions
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
    root.after(700, lambda: speak(currentJoke[0]))

# This Function works when the Show Punchline Button Is Pressed.
# It checks if the Joke is available or not. If there's no joke yet, it tells the user there isn't any.
# But when there is, it shows the punchline
def showPunchLine():
    if not currentJoke:
        canvas.create_text(250,200, text="No Joke Yet",font=("Arial",16),fill="white",width=200,tags="punchText")
        return
    
    canvas.delete("punchText")
    canvas.create_text(250,230, text=currentJoke[1],font=("Arial",16),fill="white",width=200,tags="punchText")
    speak(currentJoke[1])
    root.after(1200, laughSfx)

# Improvements :
# Layout can be changed in the Display Joke Screen.(Done)
# Music and Sfx(Done)
# Maybe an add joke Function if thats possible? So the user can add Jokes if they want in the txt file.
# Probably Python Text To Speech(Fixed)

# Start Program
displayMenu()
root.mainloop()