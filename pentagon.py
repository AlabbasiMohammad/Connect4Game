from turtle import *
import turtle


MovingTurtle =  Turtle()

MovingTurtle.begin_fill()
MovingTurtle.color('red', 'blue')
for _ in range(8):
    MovingTurtle.left(45); MovingTurtle.fd(100)
MovingTurtle.end_fill()
done()