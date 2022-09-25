#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#/\ - AND
#\/ - OR
#¬ - NOT
x = int(input('Введите число 1: '))
y = int(input('Введите число 2: '))
z = int(input('Введите число 3: '))
if (not (x or y or z)) == (not x and not y and not z):
    print(True)
else:
    print(False)