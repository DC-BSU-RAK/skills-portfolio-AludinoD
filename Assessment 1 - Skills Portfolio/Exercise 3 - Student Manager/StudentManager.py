# Assessment 3
# Student Manager
# The Theme of this app is inspired by BathSpa University.
# By : Deniz Marc Andrei Aludino
# Notes : 
# Codes from previous exercises will be used here again. Especially the one in the Alexa because of the file handling.
# I Added A Tree View, its like an excel grid that I found out that I can use in Tkinter.

from tkinter import * # Main Tkinter Program
from tkinter import ttk,messagebox,simpledialog
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
    btn = Button(root, text=text,font=("Arial", 12), width=20,command=command, bg="#23314F", fg="#FFFFFF", activebackground="#195598", cursor="hand2")

    btn.bind("<Enter>", lambda e: btn.config(bg="#195598"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#23314F"))
    return btn

# Tools
def clearCanvas():
    canvas.delete("all")

# Function for Opening and Analyzing the file.
def loadMarks():
    # Opens the File and ensures that there aren't any spaces or anything that can mess up the data.
    try:
        with open ("studentMarks.txt","r") as f:
            lines = f.read().strip().split("\n")
    # Tells if the File can't be found.
    except FileNotFoundError:
        print("File Not Found.")
        return[]
    
    # Ignores the first Line because for some reason theres a 10 there.
    lines = lines[1:]

    # Creates an empty students list that splits the parts into different variables
    # id,name,test1,test2,test3, and exam.
    students = []
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 6:
            continue
        id_,name,t1,t2,t3,exam = parts
        t1,t2,t3,exam = int(t1),int(t2),int(t3),int(exam)
        students.append([id_,name,t1,t2,t3,exam])

    return students

def saveMarks(students):
    # Access the txt file and write the student's informations in the file.
    with open ("studentsMarks.txt","w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            f.write(f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]},{s[5]}\n")

# Grade Computation
# Since there are 3 course works and 1 exam, the values are extracted from the loadMarks() Function. Then those values gets run into this code to produce the average grade.
# This function checks the student's record from 3 of their course works, adding them all to get the average.
def coursework(s):
    return s[2] + s[3] + s[4]

# This function converts the course work grades into percentage that will be have its values later.
# Total Course work + exam = 160
#  Total / 160 * 100 to get the percentage then the 2 is for the decimal places.
def convertPercent(s):
    return round((coursework(s) + s[5]) / 160 * 100, 2)

# Gets grade and checks the Letter Grade
def grade(percentage):
    if percentage >=70:
        return "A"
    if percentage >=60:
        return "B"
    if percentage >=50:
        return "C"
    if percentage >=40:
        return "D"
    return "F"

# Tree View(Like an Excel Sheet on the right side)
def createTree():
    global tree
    tree = ttk.Treeview(root,columns =("id","name","courses","exam","percentage","grades"),show="headings",height=15)

    # Headers
    tree.heading("id", text="ID")
    tree.heading("name", text="Name")
    tree.heading("courses", text="Coursework")
    tree.heading("exam", text="Exam")
    tree.heading("percentage", text="Overall %")
    tree.heading("grades", text="Grade")

    # Columns
    tree.column("id", width=70)
    tree.column("name", width=180)
    tree.column("courses", width=100)
    tree.column("exam", width=70)
    tree.column("percentage", width=80)
    tree.column("grades", width=60)

    canvas.create_window(580,290,window=tree)


# Function for Adding Data into the Tree(Excel)
def loadIntoTree(data):
    tree.delete(*tree.get_children())
    for s in data:
        courses = coursework(s)
        percentage = convertPercent(s)
        grades = grade(percentage)
        tree.insert("", END, values=(s[0], s[1], f"{courses}/60", s[5], percentage, grades))



# Main Menu Screen
def displayMenu():
    clearCanvas()
    # Bg
    canvas.create_image(0, 0, image=bgImg,anchor="nw")

    #Title
    canvas.create_text(450, 45, text="Student Manager", font=("Arial", 32, "bold"), fill="white")
    createTree()
    # Buttons
    canvas.create_window(150, 120, window=buttonStyle("View All Student Record",lambda:allStudent()))
    canvas.create_window(150, 170, window=buttonStyle("View A Student Record",lambda:studentRecord()))
    canvas.create_window(150, 220, window=buttonStyle("Show Highest Mark",lambda:highestMark()))
    canvas.create_window(150, 270, window=buttonStyle("Show Lowest Mark",lambda:lowestMark()))
    canvas.create_window(150, 320, window=buttonStyle("Sort Student Record",lambda:sortStudent()))
    canvas.create_window(150, 370, window=buttonStyle("Add Student Record",lambda:addRecord()))
    canvas.create_window(150, 420, window=buttonStyle("Delete Student Record",lambda:deleteRecord()))
    canvas.create_window(150, 470, window=buttonStyle("Update Student Record",lambda:updateRecord()))


# Functions
# Load all Student Data
def allStudent():
    data = loadMarks()
    loadIntoTree(data)

# Load Only 1 Student that the user is looking for, by using either ID or Name.
def studentRecord():
    # Search Box that stores the user input. Stores the Name or ID
    search = simpledialog.askstring("Search", "Enter ID or Name:")
    # If the user didn't type anything, the tab just closes.
    if not search:
        return
    # Case Sensitive
    search = search.casefold()

    # Loads the Data and checks if the student name or ID exists in the List. Value 0(1) for ID and 1(2) for Name.
    data = loadMarks()
    matches = [s for s in data if search in s[0].casefold() or search in s[1].casefold()]

    # Checks if the user input matches the student in the list.
    # If not found, display info.
    if not matches:
        messagebox.showinfo("Not Found", "Student Not Found.")
        return
    
    # Adds data to the tree.
    loadIntoTree(matches)

# With The use of min and max values of python, I can easily show the highest and lowest marks by going through the data percentages and choosing the highest/lowest values.
# Highest Marks
def highestMark():
    data = loadMarks()
    highest = max(data,key=lambda s:convertPercent(s))
    loadIntoTree([highest])

# Lowest Marks
def lowestMark():
    data = loadMarks()
    lowest = min(data,key=lambda s:convertPercent(s))
    loadIntoTree([lowest])

def sortStudent():
    # Same logic with looking for a student, it stores the user answer, either 1 or 2. If not then it tells them only 1 and 2 are allowed.
    sort = simpledialog.askstring("Sort Students", "1 = Ascending \n2 = Descending")
    if not sort:
        return
    
    # Checks user input if its 1, show all the data in Ascending Order
    data = loadMarks()
    if sort == "1":
        data.sort(key=lambda s: convertPercent(s))
    
    # If its 2 then we reverse the list.
    elif sort =="2":
        data.sort(key=lambda s: convertPercent(s), reverse=True)
    else:
        messagebox.showinfo("Invalid Input", "Choose 1 or 2.")

    loadIntoTree(data)

# Adding More Student Record Function
def addRecord():
    # Store Student Name
    name = simpledialog.askstring("Add Student", "Name:")
    if not name:
        return
    # T = Test
    # Gets Values from the 3 tests and exams the student has. It then computes the grade for the student using the coursework(), convertPercent(), and Grade() functions
    try:
        t1 = int(simpledialog.askstring("Test 1", "Test 1 Score 0-20:"))
        t2 = int(simpledialog.askstring("Test 2", "Test 2 Score 0-20:"))
        t3 = int(simpledialog.askstring("Test 3", "Test 3 Score 0-20:"))
        exam = int(simpledialog.askstring("Exam", "Exam Score 0-100:"))
    except:
        # If the values aren't integers
        messagebox.showerror("Invalid Input", "Marks should only be numbers.")
        return
    
    data = loadMarks()
    # Create a new ID 
    newID = str(max(int(s[0]) for s in data) + 1)
    
    # Adds the new Data to the tree using the saveMarks() function
    data.append([newID,name,t1,t2,t3,exam])
    saveMarks(data)
    messagebox.showinfo("Student Added","Student Record Added Successfully.")
    loadIntoTree(data)

# Delete Student Record
def deleteRecord():
    # Store student name or ID
    delete = simpledialog.askstring("Delete Student", "Enter ID or Name:")
    if not delete:
        return
    delete = delete.casefold()
    
    # Check if student is in the list.
    data = loadMarks()
    new = [s for s in data if delete not in s[0].casefold() and delete not in s[1].casefold()]

    # If student not found in list, tell user.
    if len(new) == len(data):
        messagebox.showinfo("Student Not Found", "No Matching Student.")
        return
    
    saveMarks(new)
    messagebox.showinfo("Student Deleted","Student Record Deleted Successfully.")
    loadIntoTree(new)


def updateRecord():
    pass

displayMenu()
root.mainloop()