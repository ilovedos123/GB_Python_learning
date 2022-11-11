# -*- mode: python ; coding: utf-8 -*-
import telebot
from telebot import types
import generator

bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('Новый справочник')
    btn_2 = types.KeyboardButton('Импорт справочника из файла')
    markup.add(btn_1, btn_2)
    bot.send_message(message.chat.id, 'Выберите нужное дейтвие', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Новый справочник':
        sent = bot.send_message(message.chat.id, 'Введите количество строк')
        bot.register_next_step_handler(sent, review)
    elif message.text == 'Импорт справочника из файла':
        imp = bot.send_message(message.chat.id, 'Введите название файла из которого необходимо импортировать список в формате "filename.csv"')
        bot.register_next_step_handler(imp, make_import)
    elif message.text == 'Показать текущий справочник':
        bot.send_message(message.chat.id, telephone_book)
    elif message.text == 'Экспорт текущего справочника в файл':
        phone_book = list(telephone_book.split())
        with open(r"phone_book.csv", "w") as file:
            count = 0
            while count < len(phone_book):
                file.write(
                    f'{phone_book[count]} {phone_book[count + 1]} {phone_book[count + 2]} {phone_book[count + 3]} {phone_book[count + 4]} {phone_book[count + 5]}''\n')
                count = count + 6
        bot.send_message(message.chat.id, 'Справочник экспортирован в файл phone_book.csv')

def review(message):
    global telephone_book
    N = int(message.text)
    telephone_book = ''
    for i in range(1, N + 1):
        telephone_book = telephone_book + f'{i} {generator.get_name()} {generator.get_surname()} {generator.get_birthdate()} {generator.get_job_city()} {generator.get_phone_number()}\n'

    bot.send_message(message.chat.id, telephone_book)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('Да')
    btn_2 = types.KeyboardButton('Нет')
    markup.add(btn_1, btn_2)
    msg = bot.send_message(message.chat.id, 'Сделать экспорт данного списка в файл?', reply_markup=markup)
    bot.register_next_step_handler(msg, bot_export_message)

def bot_export_message(message):
    if message.text == 'Да':
        phone_book = list(telephone_book.split())
        with open(r"phone_book.csv", "w") as file:
            count = 0
            while count < len(phone_book):
                file.write(
                    f'{phone_book[count]} {phone_book[count + 1]} {phone_book[count + 2]} {phone_book[count + 3]} {phone_book[count + 4]} {phone_book[count + 5]}''\n')
                count = count + 6

        bot.send_message(message.chat.id, 'Справочник экспортирован в файл phone_book.csv')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Новый справочник')
        btn_2 = types.KeyboardButton('Импорт справочника из файла')
        btn_3 = types.KeyboardButton('Показать текущий справочник')
        markup.add(btn_1, btn_2, btn_3)
        bot.send_message(message.chat.id, 'Выберите нужное дейтвие', reply_markup=markup)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Справочник сгенерирован но не экспортирован')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('Новый справочник')
        btn_2 = types.KeyboardButton('Импорт справочника из файла')
        btn_3 = types.KeyboardButton('Показать текущий справочник')
        btn_4 = types.KeyboardButton('Экспорт текущего справочника в файл')
        markup.add(btn_1, btn_2, btn_3, btn_4)
        bot.send_message(message.chat.id, 'Выберите нужное дейтвие', reply_markup=markup)
def make_import(message):
    global telephone_book
    telephone_book = ''
    file_name = message.text
    file = open(file_name, 'r')
    for line in file:
        telephone_book = telephone_book + line
    bot.send_message(message.chat.id, f'Импортирован файл {file_name}')
    bot.send_message(message.chat.id, telephone_book)
    file.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('Новый справочник')
    btn_2 = types.KeyboardButton('Импорт справочника из файла')
    btn_3 = types.KeyboardButton('Показать текущий справочник')
    btn_4 = types.KeyboardButton('Экспорт текущего справочника в файл')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    bot.send_message(message.chat.id, 'Выберите нужное дейтвие', reply_markup=markup)

bot.polling(none_stop=True, interval=0)