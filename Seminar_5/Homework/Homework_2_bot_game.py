# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint
def subtraction(total, step):  #создаем функцию, которая вычитает ход игрока из общего количества конфет
    total = total - step
    return total
number_of_candies = 100             #начальное(общее) количество конфет
and_the_winner_is = 1               #переменная для обозначения победителя
while number_of_candies > 0:        #создаем цикл, пока количество конфет больше нуля продолжаем игру
    player_1 = int(input('Игрок, введите число от 1 до 28 : '))
    if 28 > player_1 > 1:
        number_of_candies = subtraction(number_of_candies, player_1)
    else:
        while player_1 < 1 or player_1 > 28:
            print('Число должно быть от 1 до 28')
            player_1 = int(input('Игрок, введите число от 1 до 28 : '))
        number_of_candies = subtraction(number_of_candies, player_1)
    print(f'На столе осталось {number_of_candies} конфет(а)')
    and_the_winner_is = 1
    if number_of_candies > 0:
        if number_of_candies <= 57 and number_of_candies > 29:   # Добавил условие боту, чтобы на предпоследнем ходу появился "интеллект"
            player_2 = number_of_candies - 29
        elif number_of_candies <= 28:                            # Условие, что если число конфет меньше 28, то бот вынужден забирать их все
            player_2 = number_of_candies
        else:
            player_2 = randint(1, 28)                           # Ход бота без "интеллекта"
        print(f'Бот выбирает {player_2} конфет(ы)')
        number_of_candies = subtraction(number_of_candies, player_2)
        print(f'На столе осталось {number_of_candies} конфет(а)')
        and_the_winner_is = 2
    else:
        and_the_winner_is = 1
if and_the_winner_is == 1:
    print('Победил игрок')
else:
    print('Победил бот')