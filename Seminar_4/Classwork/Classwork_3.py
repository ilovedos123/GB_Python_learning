# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
a = int(input('Введите число A : '))
b = int(input('Введите число B : '))
if a > b:
    max = a
    min = b
else:
    max = b
    min = a
end = max % min
while end != 0:
    max = min
    min = end
    end = max % min
nod = min
nok = (a * b) / nod
print(nok)



#print(min)

