from turtle import *
import turtle
wn = turtle.Screen()
wn.bgcolor('green')
# turtle players
player_1 = turtle.Turtle()
def turnleft():
    player_1.left(50)
player_1.shape('circle')
#player_1.penup()
player_1.color('red')
def turnRight():
    player_1.right(50)
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnRight, "Right")
while True:
    player_1.forward(1)
done()






