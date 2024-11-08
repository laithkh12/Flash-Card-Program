# 🇫🇷 French Flash Card App

- **This Flash Card App** is an interactive way to learn French vocabulary, built with Python’s tkinter GUI library. The app displays French words, then flips to reveal the English translation after a few seconds. You can keep track of known and unknown words, allowing you to focus on words you haven’t mastered yet.

---
## 📂 Project Structure
- **Flash Card Flip**: Shows a French word, then flips to reveal the English translation after 3 seconds.
- **Learning Progress**: Keeps track of words you’ve marked as "known," saving only unknown words to words_to_learn.csv for future practice.
- **User Interface**: Simple UI with buttons to mark words as "known" or "unknown."

---
## 🔧 Code Explanation
### 1. Data Initialization
```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    originalData = pandas.read_csv("data/french_words.csv")
    toLearn = originalData.to_dict(orient="records")
else:
    toLearn = data.to_dict(orient="records")
```
- **Explanation**: Checks if a words_to_learn.csv file already exists to load your saved progress. If the file is missing, it loads french_words.csv, which contains the original list of words to learn.

### 2.Showing the Next Card
```python
def nextCard():
    global currentCard, flipTimer
    window.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)
    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=f"{currentCard['French']}", fill="black")
    canvas.itemconfig(cardBackground, image=cardFrontImg)
    flipTimer = window.after(3000, func=flipCard)
```
- **Explanation**: Randomly selects a French word from toLearn and displays it. After a 3-second delay, the card flips to reveal the English translation.

### 3. Flipping the Card
```python
def flipCard():
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=f"{currentCard['English']}", fill="white")
    canvas.itemconfig(cardBackground, image=cardBackImage)
```
- **Explanation**: Changes the card display to show the English translation.

### 4. Marking a Word as Known
```python
def isKnown():
    toLearn.remove(currentCard)
    data = pandas.DataFrame(toLearn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nextCard()
```
- **Explanation**: Removes the current word from the toLearn list, updates the words_to_learn.csv file, and then displays the next card.
---
## 🖥️ UI Setup
The tkinter interface is designed to display flashcards with simple and intuitive controls.
```python
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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
```
---
## 🚀 How to Run
1. Install Required Libraries:
```bash
pip install pandas
```
2. Save the Images:
- Ensure you have the following images in an images/ directory:
  - card_front.png - Front side of the flashcard.
  - card_back.png - Back side of the flashcard.
  - wrong.png - Image for marking an unknown word.
  - right.png - Image for marking a known word.
3. Run the Application:
```bash
python main.py
```
4. Using the App:
- Each time you run the app, it starts from where you left off. Mark words as known to remove them from future sessions.

## 📝 Notes
- **File Structure**:
  - french_words.csv: Contains the initial list of words.
  - words_to_learn.csv: Stores only unknown words, updating automatically based on your progress.
- **User Interaction**: The app lets you focus on unknown words by removing those you've marked as known.

## 🔗 Additional Resources
- tkinter Documentation
- pandas Documentation
- Random Module Documentation
