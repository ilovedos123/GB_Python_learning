# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
#  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
number_list = []
a = int(input('Введите количество элементов списка : '))
if a < 0:
    a = -a
for i in range(a):
    number_list.append(randint(1, 9))
print(number_list)
result = 0
for j in range(len(number_list)):
    if j % 2 != 0:
        result = result + number_list[j]
print(result)
