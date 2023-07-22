from tkinter import ttk, messagebox
from src.utils import *
from random import randint


def setup_horse():
    global state01, state02, state03, state04
    global weather, time_day
    global win_coefficient01, win_coefficient02, win_coefficient03, win_coefficient04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fast_speed01, fast_speed02, fast_speed03, fast_speed04

    weather = randint(1, 5)
    time_day = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    win_coefficient01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    win_coefficient02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    win_coefficient03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    win_coefficient04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fast_speed01 = False
    fast_speed02 = False
    fast_speed03 = False
    fast_speed04 = False


def win_round(horse):
    global x01, x02, x03, x04, money
    result = 'К финишу пришла лошадь '
    if horse == 1:
        result += name_horse01
        win = summ01.get() * win_coefficient01
    elif horse == 2:
        result += name_horse02
        win = summ02.get() * win_coefficient02
    elif horse == 3:
        result += name_horse03
        win = summ03.get() * win_coefficient03
    elif horse == 4:
        result += name_horse04
        win = summ04.get() * win_coefficient04
    if horse > 0:
        result += f'! Вы выиграли {int(win)}'
        if win > 0:
            insert_text(text_diary, f'Этот забег принёс Вам {int(win)}')
        else:
            result += 'К сожалению, ваша ставка не сыграла.'
        messagebox.showinfo('РЕЗУЛЬТАТ', result)
    else:
        messagebox.showinfo('Забег признан не состоявшимся', 'До финиша никто не дошёл')
        insert_text(text_diary, 'Забег признан не состоявшимся.')
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    save_money(int(money))

    setup_horse()

    start_button['state'] = 'normal'
    bet_01['state'] = 'readonly'
    bet_02['state'] = 'readonly'
    bet_03['state'] = 'readonly'
    bet_04['state'] = 'readonly'
    bet_01.current(0)
    bet_02.current(0)
    bet_03.current(0)
    bet_04.current(0)

    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horse_place_in_window(horse01, x01, horse02, x02, horse03, x03, horse04, x04)

    refresh_combo("")
    view_weather(text_diary, time_day, weather)
    health_horse()
    insert_text(text_diary, f'Ваши средства: {int(money)}')

    if money < 1:
        messagebox.showinfo("Игра остановлена")
        exit()


def health_horse():
    insert_text(text_diary, get_health(name_horse01, state01, win_coefficient01))
    insert_text(text_diary, get_health(name_horse02, state02, win_coefficient02))
    insert_text(text_diary, get_health(name_horse03, state03, win_coefficient03))
    insert_text(text_diary, get_health(name_horse04, state04, win_coefficient04))


def run_horse():
    global money
    start_button['state'] = 'disabled'
    bet_01['state'] = 'disabled'
    bet_02['state'] = 'disabled'
    bet_03['state'] = 'disabled'
    bet_04['state'] = 'disabled'
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    move_horse()


def problem_horse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global state01, state02, state03, state04
    global fast_speed01, fast_speed02, fast_speed03, fast_speed04

    horse = randint(1, 4)

    max_rand = 10000

    if horse == 1 and play01 and x01 > 0:
        if randint(0, max_rand) < state01 * 5:
            reverse01 = not reverse01
            messagebox.showinfo('', f'Лошадь {name_horse01} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state01 * 5:
            play01 = False
            messagebox.showinfo('', f'Лошадь {name_horse01} остановилась!')
        elif randint(0, max_rand) < state01 * 5 and not fast_speed01:
            fast_speed01 = True
            messagebox.showinfo('', f'Лошадь {name_horse01} ускоряется!')
    elif horse == 2 and play02 and x02 > 0:
        if randint(0, max_rand) < state02 * 5:
            reverse02 = not reverse02
            messagebox.showinfo('', f'Лошадь {name_horse02} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state02 * 5:
            play02 = False
            messagebox.showinfo('', f'Лошадь {name_horse02} остановилась!')
        elif randint(0, max_rand) < state02 * 5 and not fast_speed01:
            fast_speed02 = True
            messagebox.showinfo('', f'Лошадь {name_horse02} ускоряется!')
    elif horse == 3 and play03 and x03 > 0:
        if randint(0, max_rand) < state03 * 5:
            reverse03 = not reverse03
            messagebox.showinfo('', f'Лошадь {name_horse03} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state03 * 5:
            play03 = False
            messagebox.showinfo('', f'Лошадь {name_horse03} остановилась!')
        elif randint(0, max_rand) < state03 * 5 and not fast_speed01:
            fast_speed03 = True
            messagebox.showinfo('', f'Лошадь {name_horse03} ускоряется!')
    elif horse == 4 and play04 and x04 > 0:
        if randint(0, max_rand) < state04 * 5:
            reverse04 = not reverse04
            messagebox.showinfo('', f'Лошадь {name_horse04} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state04 * 5:
            play04 = False
            messagebox.showinfo('', f'Лошадь {name_horse04} остановилась!')
        elif randint(0, max_rand) < state04 * 5 and not fast_speed01:
            fast_speed04 = True
            messagebox.showinfo('', f'Лошадь {name_horse04} ускоряется!')


def move_horse():
    global x01, x02, x03, x04

    if randint(0, 100) < 20:
        problem_horse()

    speed01 = (randint(1, time_day + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, time_day + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, time_day + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, time_day + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    multiple = 1.5

    speed01 *= randint(1, 2 + state01) * (1 + fast_speed01 * multiple)
    speed02 *= randint(1, 2 + state02) * (1 + fast_speed02 * multiple)
    speed03 *= randint(1, 2 + state03) * (1 + fast_speed03 * multiple)
    speed04 *= randint(1, 2 + state04) * (1 + fast_speed04 * multiple)

    if play01:
        if not reverse01:
            x01 += speed01
        else:
            x01 -= speed01

    if play02:
        if not reverse02:
            x02 += speed02
        else:
            x02 -= speed02

    if play03:
        if not reverse03:
            x03 += speed03
        else:
            x03 -= speed03

    if play04:
        if not reverse04:
            x04 += speed04
        else:
            x04 -= speed04

    horse_place_in_window(horse01, x01, horse02, x02, horse03, x03, horse04, x04)
    all_play = play01 or play02 or play03 or play04
    all_x = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    all_reverse = reverse01 and reverse02 and reverse03 and reverse04

    if not all_play or all_x or all_reverse:
        win_round(0)
        return 0

    if x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952:
        root.after(5, move_horse)
    else:
        if x01 >= 952:
            win_round(1)
        if x02 >= 952:
            win_round(2)
        if x03 >= 952:
            win_round(3)
        if x04 >= 952:
            win_round(4)


def refresh_combo(event):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    money_label['text'] = f"У вас на счету:{int(money - summ)}."

    bet_01['values'] = get_values(int(money - summ02.get() - summ03.get() - summ04.get()))
    bet_02['values'] = get_values(int(money - summ01.get() - summ03.get() - summ04.get()))
    bet_03['values'] = get_values(int(money - summ01.get() - summ02.get() - summ04.get()))
    bet_04['values'] = get_values(int(money - summ01.get() - summ02.get() - summ03.get()))

    if summ > 0:
        start_button['state'] = 'normal'
    else:
        start_button['state'] = 'disabled'

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

reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False
play01 = True
play02 = True
play03 = True
play04 = True
fast_speed01 = False
fast_speed02 = False
fast_speed03 = False
fast_speed04 = False

default_money = 10000
weather = randint(1, 5)
time_day = randint(1, 4)

state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

win_coefficient01 = int(100 + randint(1, 30 + state01 * 60)) / 100
win_coefficient02 = int(100 + randint(1, 30 + state02 * 60)) / 100
win_coefficient03 = int(100 + randint(1, 30 + state03 * 60)) / 100
win_coefficient04 = int(100 + randint(1, 30 + state04 * 60)) / 100

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
start_button['state'] = 'disabled'

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
horse01_game.set(0)
horse01_check = Checkbutton(text=name_horse01, variable=horse01_game, onvalue=1, offvalue=0)
horse01_check.place(x=150, y=448)

horse02_game = BooleanVar()
horse02_game.set(0)
horse02_check = Checkbutton(text=name_horse02, variable=horse02_game, onvalue=1, offvalue=0)
horse02_check.place(x=150, y=478)

horse03_game = BooleanVar()
horse03_game.set(0)
horse03_check = Checkbutton(text=name_horse03, variable=horse03_game, onvalue=1, offvalue=0)
horse03_check.place(x=150, y=508)

horse04_game = BooleanVar()
horse04_game.set(0)
horse04_check = Checkbutton(text=name_horse04, variable=horse04_game, onvalue=1, offvalue=0)
horse04_check.place(x=150, y=538)

horse01_check['state'] = 'disabled'
horse02_check['state'] = 'disabled'
horse03_check['state'] = 'disabled'
horse04_check['state'] = 'disabled'

bet_01 = ttk.Combobox(root)
bet_02 = ttk.Combobox(root)
bet_03 = ttk.Combobox(root)
bet_04 = ttk.Combobox(root)

bet_01["state"] = "readonly"
bet_01.place(x=280, y=450)


bet_02["state"] = "readonly"
bet_02.place(x=280, y=480)


bet_03["state"] = "readonly"
bet_03.place(x=280, y=510)


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

start_button['command'] = run_horse

view_weather(text_diary, time_day, weather)
health_horse()

root.mainloop()
