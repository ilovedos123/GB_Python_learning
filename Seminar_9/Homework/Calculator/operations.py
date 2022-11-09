# -*- mode: python ; coding: utf-8 -*-

import datetime

def summ(num_1, num_2):
    return num_1 + num_2

def subtr(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def logging(name, last_name, str, num_1, num_2, answer):
    file = open('log.csv', 'a')
    file.write(f'{datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")}, {name}, {last_name},Операция: {str}, Число 1: {num_1}, Число 2: {num_2}, Ответ: {answer}\n')
    file.close()

