from tkinter import *
import math
# ---------------------------------------- Globale Variablen ---------------------------------------- #
PINK = "#e2979c"                                        # Für kurze Pause
RED = "#e7305b"                                         # Für lange Pause
GREEN = "#9bdeac"                                       # Für Arbeitsphase
YELLOW = "#f7f5dd"                                      # Hintergrundfarbe
FONT_NAME = "Courier"
WORK_MIN = 25                                           # Arbeitsphase
SHORT_BREAK_MIN = 5                                     # 5-Minuten-Pause zwischen Arbeitsphasen
LONG_BREAK_MIN = 20                                     # 20-Minuten-Pause nach 4 Arbeitsphasen
reps = 0                                                # Counter der Wiederholungen
timer = None                                            # Timer für Countdown

# -------------------------------------- Timer-Reset-Funktion ---------------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")         # Timer gibt Start im Format 00:00 aus
    title_label.config(text="Timer")                    # Titel-Label: "Timer"
    check_marks.config(text="")                         # Häkchen leer gesetzt
    global reps
    reps = 0


# -------------------------------------- Timer-Funktionsweise --------------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60                            # Zeitspanne der Arbeitsphase
    short_break_sec = SHORT_BREAK_MIN * 60              # Zeitspanne der kurzen Pause
    long_break_sec = LONG_BREAK_MIN * 60                # Zeitspanne der langen Pause

    if reps % 8 == 0:                                   # Anzahl Wiederholungen % 8, wenn True: Lange Pause
        count_down(long_break_sec)                      # Aufruf Countdown-Fkt. mit Variablen der langen Pause
        title_label.config(text="Break", fg=RED)        # Titellabel wechselt zu "Break"
    elif reps % 2 == 0:                                 # Anzahl Wiederholungen % 2, wenn Treu: Kurze Pause
        count_down(short_break_sec)                     # Aufruf Countdown-Fkt. mit Variablen der kurzen Pause
        title_label.config(text="Break", fg=PINK)       # siehe Zeile 39
    else:
        count_down(work_sec)                            # Aufruf Countdown-Fkt. mit Variablen der Arbeitsphase
        title_label.config(text="Work", fg=GREEN)       # Titellabel wechselt zu "Work"


# ------------------------------------- Countdown-Funktionsweise --------------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)                  # Minutenberechnung auf zwei Nachkommastellen
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"                     # Dynamic Typing: int-Sekundenziffern werden durch str ersetzt

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # Darstellung der Timer-Ziffern im Format 00:00
    if count > 0:                                       # Wenn > 0
        global timer
        timer = window.after(1000, count_down, count - 1) # Argumentenübergabe an count_down-Fkt. zwecks Herunterzählen
    else:
        start_timer()                                    # Ansonsten start_timer-Fkt. ausführen
        marks = ""                                       # Variable für Haken
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)                   # Setzen der Häckchen im check_marks-Feld


# --------------------------------------------- UI-Aufbau ---------------------------------------------- #
window = Tk()
window.title("Pomodoro Tomato Timer")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Tomato\nTimer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)       # Verhindern eines ungewollten Rahmens
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()










