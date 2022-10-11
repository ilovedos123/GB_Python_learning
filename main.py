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
desk_test_wrong = f'_____________\n' \
       f'| X | {table[2]} | {table[3]} |\n' \
       f'_____________\n' \
       f'| X | {table[5]} | {table[6]} |\n' \
       f'_____________\n' \
       f'| {table[7]} | X | {table[9]} |\n' \
       f'_____________'
desk_test = f'_____________\n' \
       f'| X | {table[2]} | {table[3]} |\n' \
       f'_____________\n' \
       f'| {table[4]} | X | {table[6]} |\n' \
       f'_____________\n' \
       f'| {table[7]} | {table[8]} | X |\n' \
       f'_____________'
def find_winner(board, symbol):
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

#     print(j)
    # print('____')
    # print(tuple(win_list))



print(find_winner(desk_test_wrong, 'X'))
# win_list = [24, 52, 80]
# win_combination = ((16,20,24),(44,48,52),(72,76,80),(16,44,72),(20,48,76),(24,52,80),(16,48,80),(24,48,72))
# for i in win_combination:
#     if tuple(win_list) == i:
#         print('yes')