"""3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]"""

def deleteRepeatedNumbers(list):
    l = len(list)
    list2 = []
    for i in range(l):
        n = list[i]
        f = i
        isHave = False
        for k in range(l):
            if f == k:
                continue
            if list[k] == n:
                isHave = True
                #break
        if not isHave:
            list2.append(n)
    return list2

list = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
print(deleteRepeatedNumbers(list))