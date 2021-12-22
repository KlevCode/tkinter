import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Pomodoro-Timer")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Einfügen des Logos
logo = Image.open('./large.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Anweisung, pdf-Datei auszuwählen
instructions = tk.Label(root, text="Button klicken um 25-Minuten-Timer zu starten", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# Funktion zur Auswahl der Datei über den Button
def open_file():
  browse_text.set("Laden ...")
  file = askopenfile(parent=root, mode='rb', title="Datei auswählen ...", filetypes=[("Pdf-Datei", "*.pdf")])
  if file:
    read_pdf = PyPDF2.PdfFileReader(file)
    page = read_pdf.getPage(0)
    page_content = page.extractText()

    # Textbox
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, page_content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)

    browse_text.set("Datei auswählen")

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Auswählen")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
