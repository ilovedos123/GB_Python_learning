# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037
n = int(input('Введите число : '))
list = []
result = 0
for i in range(1, n+1):
    number = (1+1/i)**i
    list.append(number)
    result = result + number
#print(list) список выводить условия не было, поэтому закомментировал
print(result)