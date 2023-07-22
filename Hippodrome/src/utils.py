from tkinter import *


def get_health(name, state, win):
    s = f'Лошадь {name} '
    if state == 1:
        s += 'просто ракета!'
    elif state == 2:
        s += 'в отличном настроении!'
    elif state == 3:
        s += 'сурова и беспощадна.'
    elif state == 4:
        s += 'чувствует себя не очень.'
    elif state == 5:
        s += 'сильно болеет'
    s += f' ({win}:1)'
    return s


def view_weather(text_diary, time_day, weather):
    s = 'Сейчас на ипподроме '
    if time_day == 1:
        s += 'ночь, '
    elif time_day == 2:
        s += 'утро, '
    elif time_day == 3:
        s += 'день, '
    elif time_day == 4:
        s += 'вечер, '

    if weather == 1:
        s += 'льёт сильный дождь.'
    elif weather == 2:
        s += 'моросит дождик.'
    elif weather == 3:
        s += 'облачно.'
    elif weather == 4:
        s += 'безоблачно, ветер.'
    elif weather == 5:
        s += 'безоблачно, прекрасная погода.'
    insert_text(text_diary, s)


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
