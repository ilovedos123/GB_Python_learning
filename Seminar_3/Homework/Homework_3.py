# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform
number_list = []
a = int(input('Введите количество элементов списка : '))
if a < 0:
    a = -a
max = 0
min = 1
for i in range(a):
    number_list.append(round(uniform(1, 15), 2))
    if round((number_list[i] - int(number_list[i])), 2) > max:
        max = round((number_list[i] - int(number_list[i])), 2)
    if round((number_list[i] - int(number_list[i])), 2) < min:
        min = round((number_list[i] - int(number_list[i])), 2)
result = round((max - min), 2)
print(number_list)
print(f'Максимальное значение дробной части элементов списка равно {max}')
print(f'Минимальное значение дробной части элементов списка равно {min}')
print(f'Разница между максимальным и минимальным значением дробной части элементов списка равно {result}')
