# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#  Пример:
#  2+2 => 4;
#  1+2*3 => 7;
#  1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример:
#  1+2*3 => 7;
#  (1+2)*3 => 9;
import re
start_string = '1+2*13'
start_string_brackets = '(1+2)*13'


# Простое решение
print(f'Решением примера {start_string} через функцию Eval: будет {int(eval(start_string))}')
print(f'Решением примера {start_string_brackets} через функцию Eval: будет {int(eval(start_string_brackets))}')

# Непростое решение
def multiplication(string):  # Функция умножения элементов, стоящих в списке полученном из функции get_list, слева и справа от знака '*'.
    string_list = get_list(string)      # А также замена этих элементов в строке string на результат умножения.
    for i in range(len(string_list) - 1):
        if string_list[i] == '*':
            break
    result = int(string_list[i - 1]) * int(string_list[i + 1])
    frag = string_list[i - 1] + string_list[i] + string_list[i + 1]    # Строка, состоящая из элементов на замену.
    string = string.replace(frag, str(int(result)), 1)
    return string

def divide(string):               # Далее функции по аналогии с умножением.
    string_list = get_list(string)
    for i in range(len(string_list) - 1):
        if string_list[i] == '/':
            break
    result = int(string_list[i - 1]) / int(string_list[i + 1])
    frag = string_list[i - 1] + string_list[i] + string_list[i + 1]
    string = string.replace(frag, str(int(result)), 1)
    return string

def plus(string):
    string_list = get_list(string)
    for i in range(len(string_list) - 1):
        if string_list[i] == '+':
            break
    result = int(string_list[i - 1]) + int(string_list[i + 1])
    frag = string_list[i - 1] + string_list[i] + string_list[i + 1]
    string = string.replace(frag, str(int(result)), 1)
    return string

def minus(string):
    string_list = get_list(string)
    for i in range(len(string_list) - 1):
        if string_list[i] == '-':
            break
    result = int(string_list[i - 1]) - int(string_list[i + 1])
    frag = string_list[i - 1] + string_list[i] + string_list[i + 1]
    string = string.replace(frag, str(int(result)), 1)
    return string

def get_solve(string):        # Функция для решения. Сначала проходим циклом по '*' и '/', затем по '+' и '-'
    for i in string:
        if i == '*':
            string = multiplication(string)
        if i == '/':
            string = divide(string)
    for i in string:
        if i == '+':
            string = plus(string)
        if i == '-':
            string = minus(string)
    return string

def brackets_solve(string):   # Функция для решения со скобками. Сначала удаляем скобки и решаем выражения в них, а затем проходим функией get_solve.
    for i in string:
        if i == '(':
            string = string.replace(i, '', 1)
            for j in string:
                if j == ')':
                    string = string.replace(j, '', 1)
        if i == '+':
            string = plus(string)
        if i == '-':
            string = minus(string)
    string = get_solve(string)
    get_solve(string)
    return string

def get_list(string):  # Функция, для перевода исходной строки в список (многозначные числа также помещаются в список)
    numbers_list = re.findall(r'\d+', string)
    operators_list = re.findall(r'\W', string)
    result_list = []
    for i in range(len(operators_list)):
        result_list.append(numbers_list[i])
        result_list.append(operators_list[i])
    result_list.append(numbers_list[i + 1])
    return result_list

print(f'Решением примера: {start_string} будет: {get_solve(start_string)}')
print(f'Решением примера: {start_string_brackets} будет: {brackets_solve(start_string_brackets)}')











