# Семинары по Python. Задачи.
## Знакомство с языком Python. 

### Семинар 1

1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет

2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

### Семинар 2

1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11

2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4)

3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072

4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.

5. Реализуйте алгоритм перемешивания списка.

## Данные, функции и модули в Python
### Семинар 3

1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10

5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

[Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:%7E:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

### Семинар 4

1. Вычислить число π c заданной точностью d

Пример: 

- при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
https://completerepair.ru/kak-vychislit-chislo-pi

2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

Пример:

- при N = 236 -> [2, 2, 59]

3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

Пример:

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9] -> [2, 4, 5, 9]

4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример: 

- k = 2 => 2 * x² + 4 * x + 5 = 0 или x² + 5 = 0 или 10 * x² = 0

5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

## Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
### Семинар 5
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

    a) Добавьте игру против бота

    b) Подумайте как наделить бота ""интеллектом""

3. Создайте программу для игры в ""Крестики-нолики"".

4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

5. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
Входные и выходные данные хранятся в отдельных текстовых файлах.

### Семинар 6

Задача: предложить улучшения кода для четырёх уже решённых задач из семинаров №№2 - 5 с помощью использования лямбд, filter, map, zip, enumerate, list comprehension
- В решении указывайте как старый вариант (до улучшения), так и новый.
- Обязательно, комментариями в коде, указывайте условие задачи.

# Python: от простого к практике

## Семинар 7

Задание в группах:
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
Программа должна уметь импортировать записи из файла, который сама экспортировала.

под форматами понимаем структуру файлов, например:
в файле на одной строке хранится одна часть записи, пустая строка - разделитель
Фамилия_1
Имя_1
Телефон_1
Описание_1
<пустая строка>
Фамилия_2
Имя_2
Телефон_2
Описание_2
<пустая строка>
и т.д.
.
или в файле на одной строке хранится все записи, символ разделитель - *;***
.
Фамилия_1,Имя_1,Телефон_1,Описание_1
Фамилия_2,Имя_2,Телефон_2,Описание_2
и т.д.
.
Обязательные пункты меню:
1 Просмотр записей
2 Добавление записи
3 Экспорт (не менее двух форматов)
4 Импорт (не менее двух форматов)
5 Выход из программы (программа должна работать, пока пользователь сам не выйдет из неё)
.
Также приветствуется:
- Поиск записи
- Удаление записи

# Семинар 8

Доделать решение задачи: Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

## Возможна ли жизнь без PIP?

### Семинар 9

1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
2. Прикрутить бота к задачам с предыдущего семинара:
- Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
- Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
