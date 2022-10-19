"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11"""

str = input("Введите число: ")
sum = 0.0
for index in str:
    #if index != ',' and index != '.':
    if index.isdigit():
        #print(index)
        sum = sum + float(index)
print(sum)
