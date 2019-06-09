from turtle import *
import  math
import turtle
def main():
    movingTurtle = turtle.Turtle()
    movingTurtle.color('#F21ED5','yellow')
    movingTurtle.speed(100)
    movingTurtle.begin_fill() #to fill the shape with the second parameters of the color function
    for i in range(400):
        movingTurtle.forward(math.sqrt(i))
        movingTurtle.left(i%170)
    movingTurtle.end_fill() # end filling the shape with a color
    movingTurtle.home()
    movingTurtle.dot(20, 'red')
    movingTurtle.penup()
    movingTurtle.back(200)
    movingTurtle.pendown()
    movingTurtle.color('#F21ED5', 'yellow')
    movingTurtle.begin_fill()  # to fill the shape with the second parameters of the color function
    for i in range(50):
        movingTurtle.forward(200)
        movingTurtle.left(170)
    movingTurtle.end_fill()
    done()
if __name__ == '__main__':
    main()