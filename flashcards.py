from tkinter import *
import pandas
import random

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/words_to_learn.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv")

    next_card()

window = Tk()
window.title("Flashcards !!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=600, width=800)
background_image = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 265, image=background_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=2)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 265, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)


right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=is_known)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
