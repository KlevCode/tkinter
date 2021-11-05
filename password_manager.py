from tkinter import *

# ---------------------------- PASSWORD-GENERATOR ------------------------------- #

# ---------------------------- SICHERES PASSWORD ------------------------------- #

# ---------------------------- UI-SETUP ------------------------------- #

white = "#ffffff"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=white)

canvas = Canvas(width=200, height=200, bg=white)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()
