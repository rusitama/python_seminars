"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

def cicleList(list):
    for i in range(len(list)):
        list[i] = round(list[i] - round(list[i]), 2)
    print(list)
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] == 0:
            continue
        if max < list[i]:
            max = list[i]
        if min > list[i]:
            min = list[i]
    return round((max - min) - round(max - min), 2)

l = [1.1, 1.2, 3.1, 5, 10.01]
print(cicleList(l))