# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import re
with open("RLE_start.txt", "r", encoding='utf-8') as file:
    text = file.readline()
#Сжатие
count = 1                    # Считаем сколько раз повторяется каждый символ в строке
count_list = []
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:   # При совпадении символов на позиции [i] и [i+1] прибавляем счетчик
        count += 1
    else:                        # При несовпадении добавляем в список count_list величину счетчика + значение первого элемента в сравнении на момент несовпадения и сбрасываем счетчик
        count_list.append(str(count) + text[i])
        count = 1
count_list.append(str(count) + text[i+1])   # Добавляем последний элемент
result = "".join(count_list)     # Преобразовываем получившийся список в строку
print(f'Результат кодирования строки {text}: {result}')
#Восстановление
k_list = re.findall(r'\d+', result) # Помещаем в список k_list все коэффициенты(числа)
decoded_result = []
for j in result:                    # Создаем список и записываем в него все буквы из закодированной строки
    if j.isdigit() == False:
        decoded_result.append(j)
total_result = []   # Создаем итоговый список и добавляем в него результаты перемножения списка с коэффициентами и списка с буквами
for k in range(len(k_list)):
    total_result.append(str(decoded_result[k])*int(k_list[k]))
total_result = "".join(total_result)         # Преобразовываем получившийся список в строку
print(f'Результат декодирования строки {result}: {total_result}')
with open("RLE_end.txt", "w", encoding='utf-8') as file:
    file.write(f'Результат кодирования строки {text}: {result}\nРезультат декодирования строки {result}: {total_result}')





