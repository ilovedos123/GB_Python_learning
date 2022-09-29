# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
n = int(input('Введите число : '))
list = []
for i in range(n):
    list.append(randint(-n, n))  #формируем список list
file = open('file.txt', 'r')     #выгружаем из файла позиции элементов в список position_list
position_list = []
for line in file:
    position = int(line.strip())
    position_list.append(position)
result = 1                      #вычисляем произведение элементов списка list на позициях position_list
for j in range(len(list)):
    for k in range(len(position_list)):
        if j == position_list[k]:
            result = result * list[j]
print(f'Произведение элементов на позициях из файла равно {result}')
print('-------------')
print(f'Список из N элементов, заполненных числами из промежутка [-N, N]: \n {list}')
print('-------------')
print(f'Позиции элементов для вычисления произведения: \n {position_list}')