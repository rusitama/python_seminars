"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11"""

strt = input("Введите число: ")
suml = 0.0
for index in strt:
    if index.isdigit():
        suml = suml + float(index)
print(suml)


# после изменения
new_sum = sum(map(float, str(strt).replace('.', '')))
print(new_sum)