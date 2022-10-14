#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = 3
xyz = ["X", "Y", "Z"]
a = []
for i in range(x):
    a.append(input(f"Введите значение {xyz[i]}: "))

result = not (xyz[0] or xyz[1] or xyz[2]) == (not xyz[0] and not xyz[1] and not xyz[2])

if result: print("Верно")
else: print("Не верно")