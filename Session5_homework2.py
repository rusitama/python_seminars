"""2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход
определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?
    a) Добавьте игру против бота
    b) Подумайте как наделить бота ""интеллектом"""""

from random import randint

def insert_number(user):
    candy = int(input(f"{user}, введите число от 1 до 28 для выбора конфет: "))
    while True:
        if candy < 1 or candy > 28:
            candy = int(input(f"{user}, введенное число не должно быть меньше 1 и больше 28 повторите еще раз: "))
        else:
            break
    return candy

def p_print(user, k, counter, value):
    print(f"Ходил {user}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

user = input("Введите ваше имя: ")
user_bot = "Bot"
candy_count = int(input("Введите количество конфет: "))

flag = randint(0, 2)
if flag:
    print(f"Первый ходит {user}")
else:
    print(f"Первый ходит {user_bot}")

counter1 = 0
counter2 = 0
while candy_count > 28:
    if flag:
        k = insert_number(user)
        counter1 += k
        candy_count -= k
        flag = False
        p_print(user, k, counter1, candy_count)
    else:
        k = randint(1,29)
        counter2 += k
        candy_count -= k
        flag = True
        p_print(user_bot, k, counter2, candy_count)

if flag:
    print(f"Выиграл {user}")
else:
    print(f"Выиграл {user_bot}")

