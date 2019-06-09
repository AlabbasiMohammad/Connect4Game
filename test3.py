import turtle
from turtle import Turtle, Screen

screen = Screen()

ru = Turtle("turtle")
ru.speed(-1)
ru.pensize(5)

def dragging(x,y):
    ru.ondrag(None)
    ru.setheading(ru.towards(x, y))
    ru.goto(x, y)
    ru.ondrag(dragging)

def clickright(x, y):
    ru.clear()

def main():
    turtle.listen()

    ru.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)

    screen.mainloop()

main()