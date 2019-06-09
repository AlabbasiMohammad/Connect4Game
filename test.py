from turtle import *
import random
#import numpy as np
import turtle

def main():
    sc = turtle.Turtle()
    sc.speed(0)
    sc.color('red')
    #sc.pensize(5)
    sc.fd(90)
    sc.shape('turtle')
    sc.left(90)
    sc.penup()
    sc.forward(100)
    sc.right(90)
    sc.pendown()
    sc.color('green')
    sc.fd(100)

    sk = turtle.Turtle()
    sk.speed(0)
    sk.color('#F21ED5', 'yellow')
    sk.begin_fill()  # to fill the shape with the second parameters of the color function
    for i in range(50):
        sk.forward(200)

        sk.left(170)
        sk.circle(90)
    sk.end_fill()



    colors = ['red', 'black', 'blue', 'yellow', 'green']
    for k in range(5):

        randColor = random.randrange(len(colors))
        sk.color(colors[randColor], colors[random.randrange(len(colors))])

        random1 = random.randrange(-300, 300)
        random2 = random.randrange(-300, 300)
        sk.penup()
        sk.setpos((random1, random2))
        sk.pendown()


        sk.begin_fill()
        sk.circle(random.randrange(80))
        sk.end_fill()
    done()
if __name__ == '__main__':main()