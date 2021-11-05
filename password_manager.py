from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD-GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- PASSWORT SPEICHERN ------------------------------- #

def save():

    website = website_entry.get()                                         # Einlesen der Daten aus Eingabefeldern
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email} "
                                 f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:                    # data.txt wird geschrieben
                data_file.write(f"{website} | {email} | {password}\n")  # Daten werden in data übergeben
                website_entry.delete(0, END)                            # Eingaben aus den Feldern löschen
                password_entry.delete(0, END)                           # Von Index 0 bis Ende


# ---------------------------- UI-SETUP ------------------------------- #

white = "#ffffff"
font_name = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=white)

canvas = Canvas(width=200, height=200, bg=white)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, pady=20)


# Label
website_label = Label(text="Webseite:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Passwort:")
password_label.grid(column=0, row=3)

# Eingaben

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35,)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "appris@gmx.net")

password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)

# Buttons

add_button = Button(text="Add", width=32, command=save)         # Save-Funktionsaufruf nach Click auf Button
add_button.grid(column=1, row=4, columnspan=2)
generate_button = Button(text="Password", width=10, command=generate_password)
generate_button.grid(column=2, row=3)



window.mainloop()
