from tkinter import ttk, messagebox
from src.utils import *


def refresh_combo(event):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    money_label['text'] = f"У вас на счету:{int(money - summ)}."

    bet_01['values'] = get_values(int(money - summ02.get() - summ03.get() - summ04.get()))
    bet_02['values'] = get_values(int(money - summ01.get() - summ03.get() - summ04.get()))
    bet_03['values'] = get_values(int(money - summ01.get() - summ02.get() - summ04.get()))
    bet_04['values'] = get_values(int(money - summ01.get() - summ02.get() - summ03.get()))

    if summ01.get() > 0:
        horse01_game.set(True)
    else:
        horse01_game.set(False)

    if summ02.get() > 0:
        horse02_game.set(True)
    else:
        horse02_game.set(False)

    if summ03.get() > 0:
        horse03_game.set(True)
    else:
        horse03_game.set(False)

    if summ04.get() > 0:
        horse04_game.set(True)
    else:
        horse04_game.set(False)


root = Tk()
WIDTH = 1024
HEIGHT = 600

x01 = 20
x02 = 20
x03 = 20
x04 = 20

name_horse01 = "Сталкер"
name_horse02 = "Прожорливый"
name_horse03 = "Ананас"
name_horse04 = "Голиаф"

default_money = 10000

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.title("ИППОДРОМ")

root.resizable(False, False)

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

road_image = PhotoImage(file="src/road.png")
road = Label(root, image=road_image)
road.place(x=0, y=17)

horse01_image = PhotoImage(file="src/horse01.png")
horse01 = Label(root, image=horse01_image)
horse02_image = PhotoImage(file="src/horse02.png")
horse02 = Label(root, image=horse02_image)
horse03_image = PhotoImage(file="src/horse03.png")
horse03 = Label(root, image=horse03_image)
horse04_image = PhotoImage(file="src/horse04.png")
horse04 = Label(root, image=horse04_image)

horse_place_in_window(horse01, x01, horse02, x02, horse03, x03, horse04, x04)

start_button = Button(text="СТАРТ", font="Arial 20 bold", width=61, background="#37AA37")
start_button.place(x=20, y=370)

text_diary = Text(width=70, height=8, wrap=WORD)
text_diary.place(x=530, y=450)

scroll = Scrollbar(command=text_diary.yview, width=20)
scroll.place(x=990, y=450, height=132)
text_diary.configure(yscrollcommand=scroll.set)

money = load_money()

if money <= 0:
    messagebox.showinfo("Игра остановлена")
    exit()

money_label = Label(text=f"Осталось средств: {money}", font="Arial 20 bold")
money_label.place(x=20, y=565)

label_horse01 = Label(text="Ставка на лошадь №1")
label_horse01.place(x=20, y=450)

label_horse02 = Label(text="Ставка на лошадь №2")
label_horse02.place(x=20, y=480)

label_horse03 = Label(text="Ставка на лошадь №3")
label_horse03.place(x=20, y=510)

label_horse04 = Label(text="Ставка на лошадь №4")
label_horse04.place(x=20, y=540)

horse01_game = BooleanVar()
horse01_game.set(False)
horse01_check = Checkbutton(text=name_horse01, variable=horse01_game, onvalue=True, offvalue=False)
horse01_check.place(x=150, y=448)

horse02_game = BooleanVar()
horse02_game.set(False)
horse02_check = Checkbutton(text=name_horse02, variable=horse02_game, onvalue=True, offvalue=False)
horse02_check.place(x=150, y=478)

horse03_game = BooleanVar()
horse03_game.set(False)
horse03_check = Checkbutton(text=name_horse03, variable=horse03_game, onvalue=True, offvalue=False)
horse03_check.place(x=150, y=508)

horse04_game = BooleanVar()
horse04_game.set(False)
horse04_check = Checkbutton(text=name_horse04, variable=horse04_game, onvalue=True, offvalue=False)
horse04_check.place(x=150, y=538)

horse01_check['state'] = 'disabled'
horse02_check['state'] = 'disabled'
horse03_check['state'] = 'disabled'
horse04_check['state'] = 'disabled'

bet_01 = ttk.Combobox(root)
bet_01["state"] = "readonly"
bet_01.place(x=280, y=450)

bet_02 = ttk.Combobox(root)
bet_02["state"] = "readonly"
bet_02.place(x=280, y=480)

bet_03 = ttk.Combobox(root)
bet_03["state"] = "readonly"
bet_03.place(x=280, y=510)

bet_04 = ttk.Combobox(root)
bet_04["state"] = "readonly"
bet_04.place(x=280, y=540)

summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

bet_01['textvariable'] = summ01
bet_02['textvariable'] = summ02
bet_03['textvariable'] = summ03
bet_04['textvariable'] = summ04

bet_01.bind("<<ComboboxSelected>>", refresh_combo)
bet_02.bind("<<ComboboxSelected>>", refresh_combo)
bet_03.bind("<<ComboboxSelected>>", refresh_combo)
bet_04.bind("<<ComboboxSelected>>", refresh_combo)

refresh_combo("")

bet_01.current(0)
bet_02.current(0)
bet_03.current(0)
bet_04.current(0)

root.mainloop()
