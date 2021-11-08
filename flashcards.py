from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------------------- UI ----------------------------------------#

window = Tk()
window.title("Flashcards !!")
window.config(padx=50, pady=50)

canvas = Canvas(height=600, width=800)
background_image = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 265, image=background_image)
canvas.grid(row=0, column=1, columnspan=2)

front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 265, image=front_image)
canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="Nederlandse Ord")
canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="Teutsch")
canvas.grid(row=0, column=1, columnspan=2)


right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(row=1, column=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=1)


window.mainloop()
