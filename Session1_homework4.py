"""Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y)."""

x = float(input(f"Введите x координату: "))
y = float(input(f"Введите y координату: "))
if x > 0:
    if y > 0: print("1")
    else: print("4")

elif y > 0: print("2")
else: print("3")