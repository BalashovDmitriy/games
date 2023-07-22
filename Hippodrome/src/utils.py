from tkinter import *


def get_values(summ):
    value = []
    if summ > 0:
        for i in range(0, 11):
            value.append(i * (int(summ) // 10))
    else:
        value.append(0)
        if summ > 0:
            value.append(summ)
    return value


def horse_place_in_window(horse01, x01, horse02, x02, horse03, x03, horse04, x04):
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)


def insert_text(text_diary, text):
    text_diary.insert(INSERT, text + "\n")
    text_diary.see(END)


def load_money(default_money=10000):
    try:
        with open("money.txt", "r") as f:
            money = int(f.read())
    except FileNotFoundError:
        print(f"Задано значение по умолчанию {default_money}")
        money = default_money
    return money


def save_money(money):
    try:
        with open("money.txt", "w") as f:
            f.write(str(money))
    except IOError:
        print("Ошибка создания файла")
        quit(1)
