# 5. Реализуйте алгоритм перемешивания списка.
from random import randint
list = [15, 0, -10, 5, -3, 2, -5, -3, 0, -15, 1, 15, -9, -7, -15]
index_list = []
while len(list) != len(index_list):  # Создаём массив произвольных, неповторяющихся индексов
    index = randint(0, len(list) - 1)
    if index in index_list:
        continue
    index_list.append(index)
result_list = []
for i in range(len(list)):                      # Заполняем итоговый массив значениями из списка list с индексами из списка index_list
    result_list.append(list[index_list[i]])
print(result_list)

