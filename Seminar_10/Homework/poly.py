# -*- mode: python ; coding: utf-8 -*-
# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import re
import telebot


bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def start(message):
     msg = bot.send_message(message.chat.id, 'Введите название файлов с первым и вторым многочленом через пробел')
     bot.register_next_step_handler(msg, poly)
@bot.message_handler(content_types=['text'])
def poly(message):
    file_name = message.text
    file_name_list = file_name.split()
    file_name_1 = file_name_list[0]
    file_name_2 = file_name_list[1]
    with open(file_name_1, "r", encoding='utf-8') as poly_1:
        p_1 = poly_1.readline()
    with open(file_name_2, "r", encoding='utf-8') as poly_2:
        p_2 = poly_2.readline()
    k_list_1 = []
    splited_p1 = p_1.split()
    for i in splited_p1:
        if i == '+' or i == '=' or i == '0':
            continue
        k_list_1.append(int(''.join(re.findall('\d', i))))
    k_list_2 = []
    splited_p2 = p_2.split()
    for j in splited_p2:
        if j == '+' or j == '=' or j == '0':
            continue
        k_list_2.append(int(''.join(re.findall('\d', j))))
    result_list = []
    for i in range(len(k_list_1)):
        result_list.append(k_list_1[i] + k_list_2[i])
    result = str(result_list[0]) + str(splited_p2[0][splited_p2[0].find('*') + 0:]) + ' + ' + str(result_list[1]) + str(splited_p2[2][splited_p2[2].find('*') + 0:]) + ' + ' + str(result_list[2])
    bot.send_message(message.chat.id, f'Результат сложения многочленов {p_1} и {p_2} равен {result}')

    with open("poly_sum.txt", "w", encoding='utf-8') as file:
        file.write(f'Результат сложения многочленов {p_1} и {p_2} равен {result}')

bot.polling(none_stop=True, interval=0)
