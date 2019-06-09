from turtle import *

import turtle

speed = 1
wn = turtle.Screen()
wn.bgcolor("black")

#players
player_1 = turtle.Turtle()
player_1.shape("circle")
player_1.color("white")
player_1.speed(0)

def turnLeft():
    player_1.left(49)
def turnright():
    player_1.right(50)
def speenUp():
    global speed
    speed += 1



turtle.listen()
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(speenUp, "Up")
while True:
    player_1.forward(speed)




done()