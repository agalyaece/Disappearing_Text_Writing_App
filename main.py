from tkinter import *

BORDER = "#3C2C3E"
FG = 'khaki'
BG = "#4B5D67"

FONT_FAMILY1 = 'Calibri'
FONT_FAMILY2 = 'Helvetica'

FONT_SIZE1 = 14
FONT_SIZE2 = 18
FONT_SIZE3 = 24

FONT_STYLE1 = 'normal'
FONT_STYLE2 = 'italic'
FONT_STYLE3 = 'bold'

PARA_FONT = (FONT_FAMILY1, FONT_SIZE1, FONT_STYLE3)
PARA_FONT2 = (FONT_FAMILY1, 12, FONT_STYLE2)
HEAD_FONT = (FONT_FAMILY2, FONT_SIZE3, FONT_STYLE1)

HEADING = "WRITE WITH MAGICAL INK"
INSTRUCTION = "If you don't press any key for 5 seconds,the text you have written will disappear"


user_text = ""
timer = None


def start_calculating(event):
    global user_text, timer

    if timer is not None:
        window.after_cancel(timer)
    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text)-1]
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)

    return


def save_text():
    global timer, user_text
    if user_text == "":
        return
    try:
        f = open("writeups.txt", "r")
    except FileNotFoundError:
        f = open("writeups.txt", "w")
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('writeups.txt', 'a') as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return


def reset_app():
    global timer, user_text
    typing_area.delete('1.0', 'end')
    user_text = ""
    timer = None
    return


window = Tk()
window.title("Disappearing text app")
window.config(padx=20, pady=20, bg=BG)
window.minsize(500, 500)

heading = Label(text=HEADING, font=HEAD_FONT, bg=BG, fg=FG, padx=10, pady=10)
heading.grid(row=0, column=0, columnspan=3)

instruction = Label(text=INSTRUCTION, font=PARA_FONT2, pady=10, fg=FG, bg=BG)
instruction.grid(row=2, column=0, columnspan=3)

typing_area = Text(font=PARA_FONT, width=100, height=15, fg=FG, bg=BG, highlightthickness=4,highlightcolor=BORDER,
                   highlightbackground=BORDER, wrap="word", padx=5, pady=5)
typing_area.bind('<KeyPress>', start_calculating)
typing_area.grid(row=3, column=0, columnspan=3)

reset_button = Button(text='Reset', fg=FG, bg=BG,font=PARA_FONT,highlightbackground=FG, highlightcolor=FG,
                      highlightthickness=0, border=3,command=reset_app, width=50)
reset_button.grid(row=4, column=0)

save_button = Button(text='Save', fg=FG, bg=BG,font=PARA_FONT, highlightbackground=FG, highlightcolor=FG,
                     highlightthickness=0, border=3,command=save_text, width=50)
save_button.grid(row=4, column=2)

window.mainloop()
