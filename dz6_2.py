# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 3, 6, 7, 2, 3, 5, 23, 13]
maxi = int(input('введите максимум: '))
mini = int(input('введите минимум: '))

def find_indeces(maxi, mini, lst):
    list_indeces = []
    for i in range(len(lst)):
        if mini <= lst[i] <= maxi:
            list_indeces.append(i)
    return list_indeces

print(f'индексы элементов массива, значения которых от {mini} до {maxi}: {find_indeces(maxi, mini, spisok)}')