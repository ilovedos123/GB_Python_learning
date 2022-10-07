# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
k = int(input('Введите степень многочлена от 1 до 9: '))
if k >= 1 and k <= 9:
    k_list = []
    for i in range(10):
        k_list.append(randint(0, 100))
    print(k_list)
    dict = {
        0: "\u2070",
        1: "\u00B9",
        2: "\u00B2",
        3: "\u00B3",
        4: "\u2074",
        5: "\u2075",
        6: "\u2076",
        7: "\u2077",
        8: "\u2078",
        9: "\u2079"
    }
    result_1 = str(k_list[randint(0,9)]) + '*x' + dict[k] + ' + ' + str(k_list[randint(0,9)]) + '*x' + dict[k-1] + ' + ' + str(k_list[randint(0,9)]) + ' = 0'
    result_2 = 'x' + dict[k]+ ' + ' + str(k_list[randint(0,9)]) + '= 0'
    result_3 = str(k_list[randint(0,9)]) + '*x' + dict[k] + '= 0'
    with open("file.txt", "w", encoding='utf-8') as file:
        file.write(result_1 + '\n' + result_2 + '\n' + result_3)
    print(f'При степени K равной {k} многочлен будет: \n {result_1} \nили: \n {result_2}\nили: \n {result_3} ')
else:
    print('Введите целое число от 1 до 9')



