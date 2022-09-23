# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#      Примеры:
#      - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
numbers_list = list(map(int, input('Введите числа через пробел: ').split()))
max = 0
for i in range(len(numbers_list)):
    if numbers_list[i] > max:
        max = numbers_list[i]
print(max)
