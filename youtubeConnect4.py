from turtle import *
import turtle
import numpy as np
import pygame
import sys


Blue = (0, 0, 255)
Black = (0, 0, 0)
row_number = 6
column_number = 7

#def creat_board():
    #board = np.zeros((row_number, column_number))
    #return board

def is_valid_location(board, col):
    return board [row_number - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(row_number):
        if board[r][col] == 0:
            return r

def drop_piece(board, raw, col, piece):
    board[raw][col] = piece

def print_board(board):
    print(np.flip(board, 0))
def winning_move(board, piece):
    # check horizontal location for win
    for c in range(column_number - 3):
        for r in range(row_number):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check vertical location for win
    for c in range(column_number):
        for r in range(row_number - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True


    # check for positively sloped diagonal
    for c in range(column_number - 3):
        for r in range(row_number - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True



    # check for negatively sloped diagonal
    for c in range(column_number - 3):
        for r in range(3, row_number):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(column_number):
        for r in range(row_number):
            pygame.draw.rect(screen, Blue, (c*squaresize, r*squaresize+squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, Black, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), Radius)





#board = creat_board()
board = np.zeros((row_number, column_number))
print_board(board)
game_over = False
turn = 0



pygame.init()

squaresize = 100
width = column_number * squaresize
height = (row_number + 1) * squaresize
size = (height , width)
Radius = int(squaresize/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)




    #ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your choice (0-6):"))
        if is_valid_location(board, col):
            raw = get_next_open_row(board, col)
            drop_piece(board, raw, col, 1)


            if winning_move(board, 1):
                print("Player 1 win")
                game_over = True


    #ask for player 2 input
    else:
        col = int(input("Player 2 make your choice (0-6):"))
        if is_valid_location(board, col):
            raw = get_next_open_row(board, col)
            drop_piece(board, raw, col, 2)


            if winning_move(board, 2):
                print("Player 2 win")
                game_over = True

    print_board(board)
    #for i in range(6):
     #   print(board[i])
      #  i +=1
    turn +=1
    turn = turn % 2