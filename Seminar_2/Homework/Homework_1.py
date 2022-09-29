# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11
a = input('Введите число : ')
try:
    result = 0
    for i in range(len(a)):
        if a[i] == ".":
            continue
        result = result + int(a[i])
    print(result)
except ValueError:
    print("Введенное значение должно состоять только из цифр")


