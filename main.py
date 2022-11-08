# -*- mode: python ; coding: utf-8 -*-
import telebot
from telebot import types


bot = telebot.TeleBot('5769693306:AAHDPx-_pcLREaLJOv48PoMpwmjToRQA_L8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.from_user.first_name)

bot.polling(none_stop=True, interval=0)