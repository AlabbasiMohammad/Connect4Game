from turtle import *
import turtle

def main():
    i = turtle.Turtle()
    i.speed(-1)
    i.color('#F21ED5','yellow')
    i.begin_fill() #to fill the shape with the second parameters of the color function
    for s in range(50):

        i.forward(200)

        i.left(170)
    i.end_fill() # end filling the shape with a color
    i.home()
    i.dot(20, 'red')

    i.penup()
    i.back(200)
    i.pendown()

    i.color('#F21ED5', 'yellow')
    i.begin_fill()  # to fill the shape with the second parameters of the color function
    for p in range(50):
        i.forward(200)

        i.left(170)
    i.end_fill()


    done()


if __name__ == '__main__':
    main()