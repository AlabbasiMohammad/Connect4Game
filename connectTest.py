from turtle import *
sc = Screen()
sc.bgcolor('red')
#sc.setworldcoordinates(0,0,200,200)
#sc.onclick()
MovingTurtle = Turtle()
MovingTurtle.speed(-1)
MovingTurtle.begin_fill()
MovingTurtle.color('#75FA9D')
MovingTurtle.penup()
MovingTurtle.setposition(-380, -310)
MovingTurtle.pendown()
for l in range(2):
    MovingTurtle.forward(750)
    MovingTurtle.left(90)
    MovingTurtle.forward(530)
    MovingTurtle.left(90)
MovingTurtle.end_fill()


MovingTurtle.penup()
MovingTurtle.forward(750)
MovingTurtle.left(90)
MovingTurtle.forward(530)


MovingTurtle.begin_fill()
MovingTurtle.color('red')
MovingTurtle.pendown()
MovingTurtle.forward(80)
MovingTurtle.left(90)
MovingTurtle.forward(750)
MovingTurtle.left(90)
MovingTurtle.forward(80)
MovingTurtle.left(90)
MovingTurtle.end_fill()


c = -265
v = -250
for j in range(6):
    MovingTurtle.penup()
    MovingTurtle.setheading(0)
    MovingTurtle.setposition(c, v)
    MovingTurtle.pendown()
    for i in range(7):
        MovingTurtle.dot(70, 'black')
        MovingTurtle.penup()
        MovingTurtle.forward(90)
        MovingTurtle.pendown()
    v += 85



sc.mainloop()