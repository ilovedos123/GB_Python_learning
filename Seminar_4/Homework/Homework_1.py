# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)
d = float(input('Введите степень точности : '))
number = input('Введите вещественное число: ')
accuracy = 0
while d < 1:
    d *= 10
    accuracy += 1
print(round(float(number), accuracy))

