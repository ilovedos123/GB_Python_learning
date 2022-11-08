# -*- mode: python ; coding: utf-8 -*-
import telebot
from telebot import types
import operations
import datetime

bot = telebot.TeleBot('5769693306:AAHDPx-_pcLREaLJOv48PoMpwmjToRQA_L8')

@bot.message_handler(commands=['start'])
def start(message):
     msg = bot.send_message(message.chat.id, 'Введите 2 числа через пробел')
     bot.register_next_step_handler(msg, show_operations)
def show_operations(message):
    global number_1
    global number_2
    user_numbers = message.text
    number_list = user_numbers.split()
    number_1 = int(number_list[0])
    number_2 = int(number_list[1])
    markup_inline = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Сложение', callback_data='summ')
    btn_2 = types.InlineKeyboardButton(text='Вычитание', callback_data='subtr')
    btn_3 = types.InlineKeyboardButton(text='Умножение', callback_data='multy')
    btn_4 = types.InlineKeyboardButton(text='Деление', callback_data='divide')
    btn_5 = types.InlineKeyboardButton(text='Выбрать другие числа', callback_data='return')
    markup_inline.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.send_message(message.chat.id, 'Выберите необходимое действие', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'summ':
        bot.send_message(callback.message.chat.id, f'{number_1} + {number_2} = {operations.summ(number_1, number_2)}')
        operations.logging(callback.message.chat.first_name, callback.message.chat.last_name, 'Сложение', number_1, number_2, operations.summ(number_1, number_2))
    elif callback.data == 'subtr':
        bot.send_message(callback.message.chat.id, f'{number_1} - {number_2} = {operations.subtr(number_1, number_2)}')
        operations.logging(callback.message.chat.first_name, callback.message.chat.last_name, 'Вычитание', number_1,
                           number_2, operations.subtr(number_1, number_2))
    elif callback.data == 'multy':
        bot.send_message(callback.message.chat.id, f'{number_1} * {number_2} = {operations.multiply(number_1, number_2)}')
        operations.logging(callback.message.chat.first_name, callback.message.chat.last_name, 'Умножение', number_1,
                           number_2, operations.multiply(number_1, number_2))
    elif callback.data == 'divide':
        bot.send_message(callback.message.chat.id, f'{number_1} / {number_2} = {operations.divide(number_1, number_2)}')
        operations.logging(callback.message.chat.first_name, callback.message.chat.last_name, 'Деление', number_1,
                           number_2, operations.divide(number_1, number_2))
    elif callback.data == 'return':
        msg = bot.send_message(callback.message.chat.id, 'Введите 2 числа через пробел')
        bot.register_next_step_handler(msg, show_operations)

bot.polling(none_stop=True, interval=0)
