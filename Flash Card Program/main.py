from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}
toLearn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    originalData = pandas.read_csv("data/french_words.csv")
    toLearn = originalData.to_dict(orient="records")
else:
    toLearn = data.to_dict(orient="records")

def nextCard():
    global currentCard, flipTimer
    window.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)
    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=f"{currentCard['French']}", fill="black")
    canvas.itemconfig(cardBackground, image=cardFrontImg)
    flipTimer = window.after(3000, func=flipCard)

def flipCard():
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=f"{currentCard['English']}", fill="white")
    canvas.itemconfig(cardBackground, image=cardBackImage)

def isKnown():
    toLearn.remove(currentCard)
    data = pandas.DataFrame(toLearn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nextCard()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipTimer = window.after(3000, func=flipCard)

canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(file="images/card_front.png")
cardBackImage = PhotoImage(file="images/card_back.png")
cardBackground = canvas.create_image(400, 263, image=cardFrontImg)
cardTitle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
cardWord = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
crossImage = PhotoImage(file="images/wrong.png")
unknownButton = Button(image=crossImage, highlightthickness=0, command=nextCard)
unknownButton.grid(row=1, column=0)

checkImage = PhotoImage(file="images/right.png")
knownButton = Button(image=checkImage, highlightthickness=0, command=isKnown)
knownButton.grid(row=1,column=1)

nextCard()








window.mainloop()
