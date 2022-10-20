"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

def cicleList(list):
    l = []
    len = len(list)
    lenth = 0
    if len % 2 == 0:
        lenth = len / 2
    else:
        lenth = round(len / 2) + 1

    for i in range(lenth - 1):
        l.append(list[i] * list[-1 * (i + 1)])
    return l

l = [2, 5, 6, 90, 76, 23, 56]
print(cicleList(l))