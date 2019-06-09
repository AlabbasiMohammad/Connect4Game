#import numpy as np
from turtle import *
import turtle
game_field = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 1],
]
print()
for i in range(6):
    print(game_field[i])

print()
print(game_field[5])
game_field.reverse()
print()
for i in range(6):
    print(game_field[i])


#print(game_field[5])

#def creat_board():
 #   board = np.zeros((5, 7))
  #  return board

#board = creat_board()
#print(board)
#creat_board()


#mo = turtle.Turtle()
#mo.penup()
#mo.setpos(-30, -130)
#mo.left(180)
#mo.forward(100)
#mo.left(90)
#mo.forward(100)
#mo.pendown()
#mo.speed(-1)
#mo.circle(200)
#done()