import pygame

def draw_grid(scr):                 # Рисование разметки
    pygame.draw.line(scr, (0,0,0), (100, 0), (100,300), 3)
    pygame.draw.line(scr, (0,0,0), (200, 0), (200,300), 3)
    pygame.draw.line(scr, (0,0,0), (0, 100), (300,100), 3)
    pygame.draw.line(scr, (0,0,0), (0, 200), (300,200), 3)

def draw_cross_zero(scr, items):    # Рисование символов
    for i in range(3):
        for j in range(3):
            if items[i][j] == '0':
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == 'x':
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)

def player_click():                 # Определения сектора по нажатию мыши
    x, y = pygame.mouse.get_pos()
    return(x//100,y//100)

def find_winner(board, symbol):     # Поиск выигрышной комбинации
    winner_founded = False
    for line in board:
        if line.count(symbol) == 3:
            winner_founded = True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            winner_founded = True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        winner_founded = True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        winner_founded = True
    return winner_founded