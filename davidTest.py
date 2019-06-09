# Connect Four - Prog0 at TU Graz SS 2019
# Name: YOUR_NAME
# Student ID: YOUR_STUDENT_ID
from math import floor, ceil
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
    print("print_field_to_console:")
    print("---------------")

    # ToDo: Some code to output the current game_field in the command line
    i = 0
    while i < len(game_field):
        j = 0
        line = "|"
        while j < len(game_field[i]):
            line = line + f'{game_field[i][j]}|'
            j = j + 1
        print(line)
        i = i + 1

    print("|A|B|C|D|E|F|G|")
    print("---------------")


def update_game_field(row_number, column_number, field, turtle):
    # This function draws the current color at
    # row_number, column_number in the field dataset with given turtle
    try:
        turtle.goto(20 + column_number * 30, 140 - row_number * 20)
        if field[row_number][column_number] == 0:
            movingTurtle.dot(70, "gray")
        if field[row_number][column_number] == 1:
            movingTurtle.dot(70, "red")
        if field[row_number][column_number] == 2:
            movingTurtle.dot(70, "blue")
    except IndexError:
        return

def check_game_winner(field):
    row_count = -1
    for row in field:
        row_count = row_count + 1
        column_count = -1
        for column in row:
            column_count = column_count + 1
            try:
                if (field[row_count][column_count]
                        == field[row_count][column_count + 1]
                        == field[row_count][column_count + 2]
                        == field[row_count][column_count + 3]
                        & field[row_count][column_count] > 0):
                    return field[row_count][column_count]
                # ToDo: Implement all rules to check whether the game is won or not

            except IndexError:
                continue
    return False

# ToDo: Display which user is next

# ToDo: Check who is the winner

def on_click_handler(x, y):
    print("Clicked on:", [x, y])
    column = floor((x * 6) / 140)
    i = 0
    while i < len(game_field):
        if game_field[i][column] > 0:
            game_field[i - 1][column] = determine_player() # TODO set the player here
            update_game_field(i - 1, column, game_field, movingTurtle)
            break
        elif i == len(game_field) - 1:
            game_field[i][column] = determine_player()  # TODO set the player here
            update_game_field(i, column, game_field, movingTurtle)
            break
        i = i + 1


    # ToDo: Handle click correctly to put a color in the game_field dataset
    # ToDo: Switch to other player so other color is played
    # ToDo: Display congratulations to winner on screen when the game is won

    print_field_to_console(game_field)

def determine_player():
    if person_to_play.pop() == 2:
        person_to_play.append(1)
        return 1
    else:
        person_to_play.append(2)
        return 2

sc = Screen()
sc.setworldcoordinates(0, 0, 200, 200)
sc.onclick(on_click_handler)

movingTurtle = Turtle()
movingTurtle.speed(10)
movingTurtle.penup()

if __name__ == '__main__':
    print("Hello World! - Console Message")

    print_field_to_console(game_field)

	# ToDo: Start game logic correctly

    sc.mainloop()