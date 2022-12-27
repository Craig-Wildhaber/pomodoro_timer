from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Courier", 35, "bold")
BUTTON_FONT = ("Courier", 15, "bold")
GREEN = "#9bdeac"
WORK_TIME_IN_SECONDS = 25 * 60
SHORT_BREAK_IN_SECONDS = 5 * 60
LONG_BREAK_IN_SECONDS = 20 * 60
reps = 1
num_of_check_marks = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global num_of_check_marks

    window.after_cancel(timer)
    top_text.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    num_of_check_marks = 0
    tomato_canvas.itemconfig(tomato_clock_text, text="00:00")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    if reps % 2 == 0:
        count_down(SHORT_BREAK_IN_SECONDS)
        top_text.config(text="Break", fg="pink")
    elif reps % 8 == 0:
        count_down(LONG_BREAK_IN_SECONDS)
        top_text.config(text="Break", fg="red")
        reps = 1
    else:
        count_down(WORK_TIME_IN_SECONDS)
        top_text.config(text="Work", fg=GREEN)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global num_of_check_marks
    global timer

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count % 60 < 10:
        count_seconds = f"0{count_seconds}"

    clock_format_count = f"{count_minutes}:{count_seconds}"

    tomato_canvas.itemconfig(tomato_clock_text, text=clock_format_count)

    if count > 0:
        timer = window.after(1_000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            num_of_check_marks += 1
            check_marks.config(text=f"{'✓' * num_of_check_marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry("500x500")
window.geometry("+700+250")
window.config(bg="black", padx=40, pady=60)
window.title("Pomodoro")

top_text = Label(text="Timer", fg=GREEN, bg="black",  font=FONT)
top_text.grid(row=0, column=1)

tomato_image = PhotoImage(file="./tomato.png")
tomato_canvas = Canvas(width=250, height=250, bg="black", highlightthickness=0)
tomato_canvas.create_image(125, 125, image=tomato_image)
tomato_clock_text = tomato_canvas.create_text(125, 150, text="00:00", fill="white", font=FONT)
tomato_canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=BUTTON_FONT, fg=GREEN, bg="black", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=BUTTON_FONT, fg=GREEN, bg="black", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", font=("Courier", 21, "bold"), fg=GREEN, bg="black", highlightthickness=0)
check_marks.grid(row=2, column=1)

window.mainloop()
