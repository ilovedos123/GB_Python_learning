# 3. Создайте программу для игры в ""Крестики-нолики"".
import sys
def find_winner(board, symbol):     # Функция поиска выигрышной комбинации
    win_list = []
    win_combination = (
    (16, 20, 24), (44, 48, 52), (72, 76, 80), (16, 44, 72), (20, 48, 76), (24, 52, 80), (16, 48, 80), (24, 48, 72))
    for i in (range(len(board))):
        if board[i] == str(symbol):
            win_list.append(i)
    for j in win_combination:
        if j == (tuple(win_list)):
            return True
            break
    else:
        return False

table = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}
desk = f'_____________\n' \
       f'| {table[1]} | {table[2]} | {table[3]} |\n' \
       f'_____________\n' \
       f'| {table[4]} | {table[5]} | {table[6]} |\n' \
       f'_____________\n' \
       f'| {table[7]} | {table[8]} | {table[9]} |\n' \
       f'_____________'
print(desk)
count = 0
already_played = []
while count < 9:
    player_1 = int(input('Выберите куда поставить Х, введите число от 1 до 9: '))
    if player_1 in already_played: # Проверка на повторение хода
        double = True
        while double == True:
            print('Ход под таким номером уже был, выберите другой номер')
            player_1 = int(input('Выберите куда поставить Х, введите число от 1 до 9: '))
            if player_1 in already_played:
                double = True
            else:
                double = False
    if player_1 >= 1 and player_1 <= 9: # Проверка на ввдение неверного числа
        desk = desk.replace(table[player_1], 'X')
        already_played.append(player_1)
        print(desk)
    else:
        while player_1 < 1 or player_1 > 9:
            print('Число должно быть от 1 до 9')
            player_1 = int(input('Выберите куда поставить Х, введите число от 1 до 9: '))
        desk = desk.replace(table[player_1], 'X')
        already_played.append(player_1)
        print(desk)
    count += 1
    if find_winner(desk, 'X') == True or find_winner(desk, '0') == True: # Проверка условия победы, после хода первого игрока
        print('Победил игрок №1')
        sys.exit()
    if count < 9:
        player_2 = int(input('Выберите куда поставить 0, введите число от 1 до 9: '))
        if player_2 in already_played: # Проверка на повторение хода
            double = True
            while double == True:
                print('Ход под таким номером уже был, выберите другой номер')
                player_2 = int(input('Выберите куда поставить 0, введите число от 1 до 9: '))
                if player_2 in already_played:
                    double = True
                else:
                    double = False
        if player_2 >= 1 and player_2 <= 9: # Проверка на ввдение неверного числа
            desk = desk.replace(table[player_2], '0')
            already_played.append(player_2)
            print(desk)
        else:
            while player_2 < 1 or player_2 > 9:
                print('Число должно быть от 1 до 9')
                player_2 = int(input('Выберите куда поставить 0, введите число от 1 до 9: '))
            desk = desk.replace(table[player_2], '0')
            already_played.append(player_2)
            print(desk)
        if find_winner(desk, 'X') == True or find_winner(desk, '0') == True: # Проверка условия победы, после хода второго игрока
            print('Победил игрок №2')
            sys.exit()
        count += 1
print('Ничья')




