"""Напишите программу, которая принимает на вход координаты двух точек и
находит расстояние между ними в 2D пространстве."""

print("Введите координаты точки А")
pointA = ["X", "Y"]
pointA[0] = int(input(f"Введите координату по точки А по x: "))
pointA[1] = int(input(f"Введите координату по точки А по y: "))

print("Введите координаты точки В")
pointB = ["X", "Y"]
pointB[0] = int(input(f"Введите координату по точки B по x: "))
pointB[1] = int(input(f"Введите координату по точки B по y: "))

lengthSegment = ((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2) ** (0.5)
print(f"Длина отрезка: {format(lengthSegment, '.2f')}")