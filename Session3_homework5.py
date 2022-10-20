"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]"""

def fibonacci(n):
    fib1 = fib2 = 1
    list = [0, 1, 1]
    list2 = []

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        list.append(fib2)

    lenth = len(list)
    for i in reversed(list):
        if i != 0 and i != 1:
            if lenth % 2 == 0:
                list2.append(i)
            else:
                list2.append(-i)
        lenth -= 1
    list2.append(-1)
    list2.append(1)

    for i in range(len(list)):
        list2.append(list[i])

    return list2

n = int(input("Введите число: "))
print(fibonacci(n))
