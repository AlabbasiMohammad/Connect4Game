from turtle import *
import turtle


game_field = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

i = 0

while i < len(game_field):
    print(i)
    i+=1

#def on_click_handler(x, y):
 #   print("Clicked on:", [x, y])

wn = turtle.Screen()
#wn.onclick(on_click_handler)
#mn = Turtle()



def glow(self,x,y):
    self.fillcolor("red")
def unglow(self,x,y):
    self.fillcolor("blue")

gh = turtle.Turtle()
gh.onclick(gh,glow)
#gh.onclick(gh.glow)
#gh.onclick(gh.unglow)
done()

