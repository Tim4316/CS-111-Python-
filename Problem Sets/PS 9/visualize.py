#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:19:56 2023

@author: hyungu
"""

import pygame
import sys
import time
from board import Board

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Define the dimensions of the board
ROWS = 6
COLS = 7
SQUARE_SIZE = 100

# Initialize Pygame
pygame.init()

# Set the size of the screen
width = COLS * SQUARE_SIZE
height = (ROWS + 1) * SQUARE_SIZE
size = (width, height)
screen = pygame.display.set_mode(size)

# Set the title of the game window
pygame.display.set_caption("Checker Game")

# Load the font for the text
font = pygame.font.SysFont(None, 75)

# Initialize the board
board = Board(ROWS, COLS)

# Draw the board
def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
            
    for row in range(ROWS):
        for col in range(COLS):
            if board.slots[row][col] == 'X':
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
            elif board.slots[row][col] == 'O':
                pygame.draw.circle(screen, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

# Update the display
def update_display(board):
    screen.fill(BLACK)
    draw_board(board)
    pygame.display.update()

# Show the text message
def show_message(text):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))
    pygame.display.update()
    time.sleep(2)

# Play the game
def play_game():
    player = 1
    game_over = False
    
    update_display(board)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player == 1:
                    col = event.pos[0] // SQUARE_SIZE
                    if board.can_add_to(col):
                        row = board.height - 1
                        while row >= 0 and board.slots[row][col] != ' ':
                            row -= 1
                        board.slots[row][col] = 'X'
                        player = 2
                else:
                    None
                    