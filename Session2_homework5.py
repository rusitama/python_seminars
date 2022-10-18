"""Реализуйте алгоритм перемешивания списка."""
import random
a = ["a", "b", "c", "d", "e", "f", "j", "h", "k", "l"]
b = []
for i in range(len(a)):
    n = random.randint(1, 10)
    isHave = False
    while True:
        for k in range(len(b)):
            if b[k] == n:
                isHave = True
        if not isHave:
            break
        else:
            n = random.randint(1, 10)
            isHave = False
    if not isHave:
        b.append(n)
c = []

for i in range(len(b)):
    c.append(a[b[i]-1])
print(b)
print(c)