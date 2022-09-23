# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#      *Примеры:*
#      - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
number = (input('Введите число: '))
dot = '.'
for i in range(len(number)):
    if number[i] == dot:
        print(number[i+1])
if dot not in number:
    print('нет')



