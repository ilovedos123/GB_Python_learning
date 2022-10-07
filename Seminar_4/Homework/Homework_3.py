# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
number_list = []
a = int(input('Введите количество элементов списка : '))
if a < 0:
    a = -a
for i in range(a):
    number_list.append(randint(1, 10))
print(f'Исходный список: {number_list}')

# Решение, если необходимо убрать из исходного списка все повторяющиеся элементы
double_index = []
for j in range(len(number_list)):
    for k in range(j+1, len(number_list)):
        if number_list[j] == number_list[k]:
            double_index.append(j)
            double_index.append(k)
unique_double_index = set(double_index)
print(f'Индексы повотряющихся элементов: {unique_double_index}')
result_list = [i for i in number_list if number_list.index(i) not in unique_double_index]
print(f'Список, в котором удалены все повторяющиеся элементы: {result_list}')

# Решение, если необходимо убрать только дубликаты, но не сами элементы, которые повторяются
unique_number_list = set(number_list)
print('_________________')
print(f'Множество неповторяющихся элементов исходного списка: {unique_number_list}')






