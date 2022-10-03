# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
a = int(input('Введите число : '))
result = ''
last_number = str(a % 2)
while a != 1:
    a = int(a/2)
    value = a % 2
    result = result + str(value)
result = result[::-1] + last_number
print(result)

