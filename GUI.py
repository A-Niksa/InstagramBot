# ---------------------------------------------------------------------------- #
#                            instagram bot frontend                            #
# ---------------------------------------------------------------------------- #

# ----------------- importing necessary modules and packages ----------------- #
import json
from tkinter import *
from PIL import ImageTk, Image
import subprocess

# --------------------------- defining bot commands -------------------------- #
def runBot():
    subprocess.call("bot.py", shell = True)
def command():
    accountsToFollow = list(entry.get().split(" "))
    with open("info.json", "r+") as jFile:
        jFileData = json.load(jFile)
        jFileData["usernames"] = accountsToFollow
        jFile.seek(0)
        json.dump(jFileData, jFile, indent = 4)
    runBot()

# ---------------------------- initializing window --------------------------- #
window = Tk()
window.iconbitmap("Resources/InstagramBot.ico")
window.title("Instagram Bot")
window.geometry("720x340")

# -------------------------- putting image on window ------------------------- #
image = ImageTk.PhotoImage(Image.open("Resources/UnsuspectingBotResized.png"))
photoLabel = Label(image = image, width = 720, height = 242)
photoLabel.image = image
photoLabel.pack()

# ------------------ displaying label and getting user input ----------------- #
textLabel = Label(text = """Please enter the desired unsernames! Note that usernames have to be delimited with exactly 1 whitespace.""",
 font = ("Arial", 11))
textLabel.pack()
entry = Entry(window, width = 450, font = ("Arial", 11))
entry.pack()
button = Button(window, text = "Follow, like, and comment!", command = command, width = 150, font = ("Arial", 11))
button.pack()

# ------------------------------ putting footer ------------------------------ #
footer = Label(text = "Created by Arsha Niksa", font = ("Arial", 7), anchor = "sw", justify = LEFT)
footer.pack()

# -------------------------------- running app ------------------------------- #
window.mainloop()