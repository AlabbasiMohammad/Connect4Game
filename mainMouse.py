from turtle import *
#from math import floor , ceil
#import sys
game_field = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],]
person_to_play = [2]
def print_field_to_console(field):
    #print("print_field_to_console:")
    print("---------------------")
    #for i in range(6):
     #   print(game_field[i])
    # ToDo: Some code to output the current game_field in the command line
    print(game_field[5])
    print(game_field[4])
    print(game_field[3])
    print(game_field[2])
    print(game_field[1])
    print(game_field[0])
    print("|A |B |C |D |E |F |G|")
    print("---------------------")
def update_game_field(row_number, column_number, field, turtle):
    # This function draws the current color at
    # row_number, column_number in the field dataset with given turtle
    try:
        turtle.goto(50 + column_number * 50, 50 + row_number * 55)
        if field[row_number][column_number] == 0:
            MovingTurtle.dot(80, "black")
        if field[row_number][column_number] == 1:
            MovingTurtle.dot(80, "red")
        if field[row_number][column_number] == 2:
            MovingTurtle.dot(80, "blue")
    except IndexError:
        return
row_number = 6
column_number = 7
def location_in_field(field, column):
    return field[row_number - 1][column] == 0

def raw_to_drop(field, column):
    for r in range(row_number):
        if field[r][column] == 0:
            return r
def brick_to_drop(field, column, raw, brick):
    field[raw][column] = brick
def on_click_handler(x, y):
    print("Clicked on:", [x, y])
    column = int(x/55)
    if location_in_field(game_field, column):
        raw = raw_to_drop(game_field, column)
        brick_to_drop(game_field, column, raw, turn())
        #game_field[raw][column] = turn()
        update_game_field(raw, column, game_field, MovingTurtle)
        print_field_to_console(game_field)
        if check_game_winner(game_field):
            if game_field[raw][column] == 1:
                print("player 1 won")
                MovingTurtle.goto(200, 260)
                MovingTurtle.color('red')
                MovingTurtle.write("Player 1 won", True, "center", ("Arial", 60, "normal"))
                #exit(sys)
            else:
                print("player 2 won")
                MovingTurtle.goto(200, 260)
                MovingTurtle.color('blue')
                MovingTurtle.write("Player 2 won", True, "center", ("Arial", 60, "normal"))

def turn():
    if person_to_play.pop() == 2:
        person_to_play.append(1)
        return 1
    else:
        person_to_play.append(2)
        return 2

# ToDo: Check who is the winner
def check_game_winner(field):
    row_count = -1
    for row_ in field:
        row_count = row_count + 1
        column_count = -1
        for column in row_:
            column_count = column_count + 1
            try:
                # check horizontal location for win
                if (field[row_count][column_count]
                        == field[row_count][column_count + 1]
                        == field[row_count][column_count + 2]
                        == field[row_count][column_count + 3]
                        & field[row_count][column_count] > 0):
                    return field[row_count][column_count]
                # ToDo: Implement all rules to check whether the game is won or not
                # check vertical location for win
                elif (field[row_count][column_count]
                        == field[row_count + 1][column_count]
                        == field[row_count + 2][column_count]
                        == field[row_count + 3][column_count]
                        & field[row_count][column_count] > 0):
                    return field[row_count][column_count]
                # check for positively sloped diagonal
                elif (field[row_count][column_count]
                        == field[row_count + 1][column_count + 1]
                        == field[row_count + 2][column_count + 2]
                        == field[row_count + 3][column_count + 3]
                        & field[row_count][column_count] > 0):
                    return field[row_count][column_count]
                # check for negatively sloped diagonal
                elif (field[row_count][column_count]
                        == field[row_count - 1][column_count + 1]
                        == field[row_count - 2][column_count + 2]
                        == field[row_count - 3][column_count + 3]
                        & field[row_count][column_count] > 0):
                    return field[row_count][column_count]
            except IndexError:
                continue
    return False
sc = Screen()
sc.setworldcoordinates(0, 0, 400, 400)
sc.bgcolor('#07E2F2')
sc.onclick(on_click_handler)
MovingTurtle = Turtle()
MovingTurtle.speed(-1)
MovingTurtle.penup()
MovingTurtle.hideturtle()
def draw_field_with_turtle():
    column = 0
    raw = 0
    for c in range(6):
        for r in range(7):
            update_game_field(raw, column, game_field, MovingTurtle)
            column += 1
        raw += 1
        column = 0

#game_over = False
#turn = 0
if __name__ == '__main__':
    print("Hello World! - Console Message")
    #while not game_over:
    sc.listen()
    print(person_to_play)
    print_field_to_console(game_field)
    draw_field_with_turtle()
    #check_game_winner(game_field)

    sc.mainloop()
#        if sc.onclick(on_click_handler):
#            print_field_to_console(game_field)
#            draw_field_with_turtle()
#            if check_game_winner(game_field):
#                print("winning")
#                game_over =True
#            sc.mainloop()
    #while not game_over:
    #    #ask plyer 1
    #    if turn == 0:
    #        print("Click on the field")
    #        MovingTurtle.goto(200, 360)
    #        MovingTurtle.color('red')
    #        MovingTurtle.write("Player 1 on", True, "center", ("Arial", 30, "normal"))
    #    else:
    #        print("Click on the field")
    #        MovingTurtle.goto(200, 360)
    #        MovingTurtle.color('blue')
    #        MovingTurtle.write("Player 2 on", True, "center", ("Arial", 30, "normal"))
    #    turn += 1
    #    turn = turn % 2

