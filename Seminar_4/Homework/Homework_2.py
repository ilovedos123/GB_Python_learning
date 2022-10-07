# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите число: '))
result = N
index = 2
multi_list = []
while result > 1:
    if result % index == 0:
        multi_list.append(index)
        result = int(result / index)
        index = 2
    else:
        index += 1
print(multi_list)



