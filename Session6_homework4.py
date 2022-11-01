"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры."""

number = int(input("Введите число: "))
a = int(input("Введите для нахождения позиции a c 0 до " + str(number * 2) + ": "))
b = int(input("Введите для нахождения позиции b c 0 до " + str(number * 2) + ": "))
l = []
n = number + 1
for i in range(number):
    l.append(-1 * (n - 1))
    n -= 1
l.append(0)
for i in range(number):
    l.append(i + 1)
print(l)
print(l[a] * l[b])

# после изменения
l = [i for i in range(-number, number + 1)]
print(l[a] * l[b])
