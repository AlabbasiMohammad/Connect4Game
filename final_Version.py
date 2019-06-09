# Connect Four - Prog0 at TU Graz SS 2019
# Name: Al-Abbasi Mohammad
# Student ID:_01514741
from turtle import *

game_field = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
person_to_play = [2]
def print_field_to_console(field):
    print("---------------------")
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
            MovingTurtle.dot(80, "yellow")
    except IndexError:
        return
row_number = 6
column_number = 7
def location_in_field(field, column):
    return field[row_number - 1][column] == 0

def row_to_drop(field, column):
    for r in range(row_number):
        if field[r][column] == 0:
            return r
def brick_to_drop(field, column, row, brick):
    field[row][column] = brick
def on_click_handler(x, y):
    print("Clicked on:", [x, y])
    column = int(x/55)
    if location_in_field(game_field, column):
        row = row_to_drop(game_field, column)
        brick_to_drop(game_field, column, row, turn_())
        update_game_field(row, column, game_field, MovingTurtle)
        print_field_to_console(game_field)
    else:
        print("The column is already occupied!")

    if check_game_winner(game_field):
            if game_field[row][column] == 1:
                print("player 1 won!")
                sc.clear()
                user_input = sc.textinput("Player 1 won!", "Type in your name")
                MovingTurtle.goto(200, 350)
                MovingTurtle.color('red')
                MovingTurtle.write("Congratulations", True, "center", ("Arial", 60, "normal"))
                MovingTurtle.goto(200, 300)
                MovingTurtle.color('red')
                MovingTurtle.write(str(user_input), True, "center", ("Arial", 60, "normal"))
                MovingTurtle.goto(200, 250)
                MovingTurtle.color('red')
                MovingTurtle.write("You won!", True, "center", ("Arial", 60, "normal"))
            else:
                print("player 2 won!")
                sc.clear()
                user_input = sc.textinput("Player 2 won!", "Type in your name")
                MovingTurtle.goto(200, 350)
                MovingTurtle.color('yellow')
                MovingTurtle.write("Congratulations", True, "center", ("Arial", 60, "normal"))
                MovingTurtle.goto(200, 300)
                MovingTurtle.color('yellow')
                MovingTurtle.write(str(user_input), True, "center", ("Arial", 60, "normal"))
                MovingTurtle.goto(200, 250)
                MovingTurtle.color('yellow')
                MovingTurtle.write("You won!", True, "center", ("Arial", 60, "normal"))
def turn_():
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
sc.bgcolor('blue')
sc.onclick(on_click_handler)
MovingTurtle = Turtle()
MovingTurtle.speed(0)
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

#if __name__ == '__main__':
    #print("Hello World! - Console Message")
    #sc.listen()
    #print(person_to_play)
    #print("Players")
    #print_field_to_console(game_field)
    #sc.tracer(0,0)
    #draw_field_with_turtle()
    #sc.update()
    #sc.mainloop()

game_over = False
turn = 0
if __name__ == '__main__':
    print("Hello World! - Console Message")

    print_field_to_console(game_field)
    draw_field_with_turtle()
	# ToDo: Start game logic correctly
    while not game_over:
        # ToDo: Display which user is next
        #ask for player 1 input
        if turn == 0:
            col = True
            while col:
                try:
                    column = int(input("Player 1 put your brick in a column (0-6):"))
                    if column < 7 and column >= -1:
                        if location_in_field(game_field, column):
                            raw = row_to_drop(game_field, column)
                            brick_to_drop(game_field, column, raw, 1)
                            col = False
                            break
                        else:
                            print("The column is already occupied.")
                    else:
                        print("Put your brick in a range of (0-6):")
                except ValueError:
                    print("Incorrect Value.Please insert a Number")
                    continue
            if check_game_winner(game_field):
                # ToDo: Display congratulations to winner on screen when the game is won
                print("Congratulations.Player 1 won")
                MovingTurtle.color('red')
                MovingTurtle.goto(200, 380)
                MovingTurtle.write("Congratulations!.Player 1 won!", True, "center",("Arial", 25, "normal"))
                game_over = True

        #ask for plyer 2 input
        else:
            col = True
            while col:
                try:
                    column = int(input("Player 2 put your brick in a column (0-6):"))
                    if column < 7 and column >= -1:
                        if location_in_field(game_field, column):
                            raw = row_to_drop(game_field, column)
                            brick_to_drop(game_field, column, raw, 2)
                            col = False
                            break
                        else:
                            print("The column is already occupied.")
                    else:
                        print("Put your brick in a range of (0-6):")
                except ValueError:
                    print("Incorrect Value.Please insert a Number")
                    continue

            if check_game_winner(game_field):
                # ToDo: Display congratulations to winner on screen when the game is won
                print("Congratulations.Player 2 won")
                MovingTurtle.color('yellow')
                MovingTurtle.goto(200, 380)
                MovingTurtle.write("Congratulations!.Player 2 won!", True, "center", ("Arial", 25, "normal"))
                game_over = True

        #game_field.reverse()
        print_field_to_console(game_field)
        update_game_field(raw, column, game_field, MovingTurtle)

        # make winning great again
        if check_game_winner(game_field):
            win_great_again = input("Enter your name :")
            MovingTurtle.goto(220, 355)
            MovingTurtle.write( win_great_again + " won!" , True, "center", ("Arial", 25, "normal"))
        turn +=1
        turn = turn % 2