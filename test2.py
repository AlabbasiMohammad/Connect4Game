import turtle

mo = turtle.Turtle()
mo.speed(0)
mo.width(5)


def up():
    mo.setheading(90)
    mo.forward(100)
def down():
    mo.setheading(270)
    mo.forward(100)
def left ():
    mo.setheading(180)
    mo.forward(100)
def right ():
    mo.setheading(0)
    mo.forward(100)

turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')


turtle.mainloop()