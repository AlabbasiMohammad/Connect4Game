from turtle import *

import turtle



def turn(x, y):
    left(180)

sc = Screen()
sc.listen()
#sc.onclick(turn)

mo= Turtle()
#mo.listen()
mo.onclick(turn(100,100))

sc.mainloop()