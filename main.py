from tkinter import *
import math
import winsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#fa0000"
YELLOW = "#f2bfe1"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20

reps = 0
timer = None

def play_alarm():
    try:
        winsound.Beep(1000, 500)
    except:
        pass

def bring_to_front():
    window.deiconify()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def open_settings():
    settings_window = Toplevel(window)
    settings_window.title("Time Settings")
    settings_window.config(padx=20, pady=20)

    Label(settings_window, text="Work (min):").grid(row=0, column=0)
    Label(settings_window, text="Short Break (min):").grid(row=1, column=0)
    Label(settings_window, text="Long Break (min):").grid(row=2, column=0)

    work_entry = Entry(settings_window, width=10)
    work_entry.insert(0, str(WORK_MIN))
    work_entry.grid(row=0, column=1)

    short_entry = Entry(settings_window, width=10)
    short_entry.insert(0, str(SHORT_BREAK_MIN))
    short_entry.grid(row=1, column=1)

    long_entry = Entry(settings_window, width=10)
    long_entry.insert(0, str(LONG_BREAK_MIN))
    long_entry.grid(row=2, column=1)

    def save_settings():
        global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
        try:
            WORK_MIN = int(work_entry.get())
            SHORT_BREAK_MIN = int(short_entry.get())
            LONG_BREAK_MIN = int(long_entry.get())
            reset_timer()
            settings_window.destroy()
        except ValueError:
            pass

    Button(settings_window, text="Save", command=save_settings).grid(row=3, column=0, columnspan=2, pady=10)

def reset_timer():
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    window.title("Pomodoro")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    window.title(f"Pomodoro - Tur {reps}")
    bring_to_front()

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        play_alarm()
        bring_to_front()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
try:
    tomato_img = PhotoImage(file="assets/tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
except:
    pass

canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

settings_button = Button(text="Settings", highlightthickness=0, command=open_settings)
settings_button.grid(column=1, row=4)

window.mainloop()