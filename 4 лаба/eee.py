import tkinter
from tkinter import *
from PIL import ImageTk, Image
import re


def change_first_with_max(numbers):
    max_index = numbers.index(max(numbers))
    if len(numbers) > 0:
        numbers[0], numbers[max_index] = numbers[max_index], numbers[0]
    return numbers


def save_number():
    global clicks
    number = str(entry.get())
    if number[0] == "0":
        number = "0"
    number = int(number)
    numbers.append(number)
    listbox.insert(END, number)
    entry.delete(0, END)
    clicks += 1
    if clicks == 10:
        show_numbers()


def show_numbers():
    global dc
    change_first_with_max(numbers)

    top = Toplevel()
    top.title("Введенные числа")
    top.geometry("600x600")
    top.configure(bg=dc)

    label = Label(top, text="Числа:", bg=dc)
    label.pack()

    if numbers.count(numbers[0]) == len(numbers):
        display = Label(top, text="Все элементы одинаковые!", bg=dc)
        display.pack()
    else:
        for number in numbers:
            display = Label(top, text=number, bg=dc)
            display.pack()


def deleting():
    global clicks, numbers
    if var.get():
        clicks = 0
        listbox.delete(0, END)
        numbers.clear()

    elif not var.get():
        clicks -= 1
        numbers = numbers[:-1]
        listbox.delete(first=0)


def update_frame(frame_num):
    gif.seek(frame_num)
    tk_image = ImageTk.PhotoImage(gif)
    canvas.create_image(0, 0, image=tk_image, anchor="nw")
    canvas.image = tk_image


def animate(frame_num=0):
    update_frame(frame_num)

    frame_num += 1
    if frame_num >= frames:
        frame_num = 0

    root.after(100, animate, frame_num)


def check_format(newval):
    result = re.match(r"^-?\d*(\.\d+)?$", newval) is not None
    if not result:
        errmsg.set("Введите число")
    else:
        errmsg.set("")
    return result



root = Tk()

var = BooleanVar()
bg_var = IntVar()
bg_var.set(0)

numbers = []
clicks = 0
dc = 'powderblue'
dfont = ("Comic Sans MS", 10, "bold")

root.title("Вариант 4")
root.geometry('3750x3000')

canvas = tkinter.Canvas(root)
canvas.pack(fill="both", expand=True)

gif = Image.open("2825710.gif")
frames = gif.n_frames

checking = (root.register(check_format), "%P")
errmsg = StringVar()

lbl1 = Label(text="Задание3750x3000\n\n"
                    "Введите целочисленный массив, состоящий из 10 элементов.\n"
                    "Поменять местами первый и максимальный элемент.", height=5, width=52, font=("Comic Sans MS", 22, "bold"), background=dc)
lbl1.place(x=500, y=100)

prompt = Label(root, text="Введите число:", height=5, width=20, font=dfont, background=dc)
prompt.place(x=500, y=370)

entry = Entry(root, foreground='black', background=dc, validate="key", validatecommand=checking)
entry.place(x=700, y=390)

error_label = tkinter.Label(foreground="red", textvariable=errmsg, wraplength=250, background=dc)
error_label.place(x=700, y=410)

button = Button(root, text="Сохранить", command=save_number, background=dc)
button.place(x=700, y=430)

listbox = Listbox(root, foreground='black', background=dc)
listbox.place(x=1000, y=370)

lbl3 = Label(text="Если нужно удалить: ", height=5, width=20, font=dfont, background=dc)
lbl3.place(x=500, y=500)

check = Checkbutton(text="Удалить всё", variable=var, background=dc)
check.place(x=700, y=520)

bnt = Button(text="Удалить", command=deleting, background=dc)
bnt.place(x=700, y=550)

animate()
root.mainloop()
