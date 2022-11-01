"""Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072"""

number = int(input("Введите число: "))

n = 0
suml = 0.0
for i in range(number):
    n += 1
    #print((1 + 1/n)**n)
    suml = suml + (1 + 1/n)**n
print(round(suml, 3))

# после изменения
list = [(1 + 1 / i) ** i for i in range(1, number + 1)]
print(round(sum(list), 3))