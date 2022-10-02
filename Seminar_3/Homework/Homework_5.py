# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
k = int(input('Введите число : '))
fibo_list = [1, 0, 1]
for i in range(1, k):
    fibo_list.append(fibo_list[i] + fibo_list[i + 1])
print(fibo_list)
fibo_list.insert(0,fibo_list[-2])
fibo_list.insert(0,-fibo_list[-1])
index = 0
while (fibo_list[index] + fibo_list[index + 1]) != 1:
    fibo_list.insert((index + 2),(fibo_list[index] + fibo_list[index + 1]))
    index += 1
print(fibo_list)





