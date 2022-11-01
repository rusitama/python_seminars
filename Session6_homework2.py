"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""

from itertools import accumulate
import operator

number = int(input("Введите число: "))
a = []
n = 0
for i in range(number):
    n += 1
    p = 1
    for k in range(n):
        p = p * (k + 1)
    a.append(p)
print(a)

# после изменения
#a = [i for i in range(1, number + 1)]
a = list(accumulate([i for i in range(1, number + 1)], operator.mul))
print(a)