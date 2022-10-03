# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
number_list = []
a = int(input('Введите количество элементов списка : '))
if a < 0:
    a = -a
for i in range(a):
    number_list.append(randint(1, 9))
print(number_list)
result_list = []
result = 1
index = -1
if (len(number_list)) % 2 == 0:
    for j in range(int(len(number_list)/2)):
        result = number_list[j] * number_list[index]
        result_list.append(result)
        index -= 1
else:
    for j in range(int(len(number_list)/2 + 1)):
        result = number_list[j] * number_list[index]
        result_list.append(result)
        index -= 1
print(result_list)




