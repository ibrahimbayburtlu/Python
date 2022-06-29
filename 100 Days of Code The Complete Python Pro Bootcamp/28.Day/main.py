from _tkinter import *
from tkinter import Canvas, PhotoImage, Tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)

canvas = Canvas(width=200,height=224)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_ing)
canvas.create_text(103,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()





window.mainloop()
