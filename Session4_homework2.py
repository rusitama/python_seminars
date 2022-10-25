"""2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59]"""

def intToNatiralList(number):
    list = []
    while True:
        if number % 2 == 0:
            list.append(2)
            number = number / 2
            print(number)
        else:
            list.append(number)
            break
    return list

n = int(input())
print(intToNatiralList(n))