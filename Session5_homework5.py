"""5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
Порядок элементов менять нельзя.
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
Входные и выходные данные хранятся в отдельных текстовых файлах."""

def get_sorted_list(list):
    tlist = [list[0]]
    for i in list:
        if i > max(tlist):
            tlist.append(i)
    return tlist

file1 = 'session5_1.txt'
file2 = 'session5_2.txt'
with open(str(file1), 'r') as data:
    l = data.read().split()
l = [int(x) for x in l]

l2 = get_sorted_list(l)
with open(file2, 'w') as data:
    data.write(str(l2))
print(l2)
