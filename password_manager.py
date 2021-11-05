from tkinter import *

# ---------------------------- PASSWORD-GENERATOR ------------------------------- #

# ---------------------------- SICHERES PASSWORD ------------------------------- #

# ---------------------------- UI-SETUP ------------------------------- #

white = "#ffffff"
font_name = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=white)

canvas = Canvas(width=200, height=200, bg=white)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# ------------------------------------ COLUMN NULL ----------------------------------------------- #

website_label = Label(text="Website", bg=white, font=(font_name, 20))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username", bg=white, font=(font_name, 20))
email_label.grid(column=0, row=2)

password_label = Label(text="Password", bg=white, font=(font_name, 20))
password_label.grid(column=0, row=3)

# ------------------------------------ COLUMN EINS ----------------------------------------------- #

website_entry = Entry(height=5, width=35, columnspan=2)
website_entry.insert(END, string="Webseite für Passwort eingeben")
website_entry.grid(column=1, row=1)

email_entry = Entry(height=5, width=35, columnspan=2)
email_entry.insert(END, string="Email/Nutzernamen zur Webseite eingeben")
email_entry.grid(column=1, row=2)

password_entry = Entry(height=5, width=21)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", height=5, width=36, columnspan=2)                       # Funktionsaufruf hinzufügen
add_button.grid(column=1, row=4)


# ------------------------------------ COLUMN ZWEI ----------------------------------------------- #

generate_button = Button(text="Generate Password", height=5, width=36, columnspan=2)      # Funktionsaufruf hinzufügen
add_button.grid(column=2, row=3)



window.mainloop()
