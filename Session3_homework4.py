"""Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10"""

def toBinary(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

n = int(input("Введите число для приоброзования в двоичное число: "))
print(toBinary(n))