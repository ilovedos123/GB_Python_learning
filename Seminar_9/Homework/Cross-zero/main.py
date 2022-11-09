# -*- mode: python ; coding: utf-8 -*-
import pygame
import operations

pygame.init()
screen_size = (300, 300)
window = pygame.display.set_mode(screen_size)
screen = pygame.Surface(screen_size)
pygame.display.set_caption('Крестики-нолики')
screen.fill((255, 255, 255))
desk = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
game_playing = True
game_over = False
turn = 0
while game_playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if desk[operations.player_click()[1]][operations.player_click()[0]] == '':
                if turn % 2 == 0:
                    desk[operations.player_click()[1]][operations.player_click()[0]] = 'x'
                else:
                    desk[operations.player_click()[1]][operations.player_click()[0]] = '0'
                turn += 1
            player_1_win = operations.find_winner(desk, 'x')
            player_2_win = operations.find_winner(desk, '0')
            if player_1_win or player_2_win:
                game_over = True
                if player_1_win:
                    pygame.display.set_caption('Победил игрок №1')
                else:
                    pygame.display.set_caption('Победил игрок №2')
            elif turn == 9:
                game_over = True
                pygame.display.set_caption('Ничья')
    operations.draw_cross_zero(screen, desk)
    operations.draw_grid(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()
