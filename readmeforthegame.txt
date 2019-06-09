Assignment tasks
For each of the following tasks you will get points depending on how well you solved them. Although all of them have the same importance regarding your grade we recommend solving them in the order provided.

Easy start - console game field: 
At first it is mandatory to create the game board. We created the data structure game_field with 7x6 rows. Have a look at the data structure and understand what 0, 1, or 2 means. Complete the print_field_to_console function.

Graphic start - turtle game field: 
At this point we want you to get familiar with turtle graphics. Have a look at update_game_field and draw the whole board in turtle graphics.

Keyboard Input:
At this point of the assignment we want to be able to play the game with our keyboard. The game should be played one player after one, so starting by asking the first player where to put the first brick, drawing it accordingly, asking the second player where to put the first brick, and so on. Find a way to let the players set their brick in a chosen field in your game board according to the coordinates
|A|B|C|D|E|F|G|

Make it more beautiful :（✿ ͡◕ ᴗ◕)つ━━✫・*。
Now that all the basic pieces are placed we want you to create more flexibility in terms of customization. Change the color of your game so that the game board has a color different than white, the bricks and the (if used) text color for Player A and Player B are different. Make it clear to the users so they know when it's their turn.

Error detection and handling - What can go wrong?:
Detect errors like when a player tries to occupy a already full column. Make sure the player order is fair and nobody takes two turns. Don't allow drawing outside the board.

Winning, the Art of loosing at Loosing:
For this task you have to implement a game logic for detecting the game state. After a player won make sure to tell the players who won. Make sure also to communicate it if a draw occurs.

But wait, I also have a mouse!
In this task we want you to add support for mouse input. The game should be playable completely with your mouse. You don't have to support the keyboard input at the same time (comment the affected lines out with an #) , but if you figure out a way to do so it would be cool.

Make winning great again:
In case of a win give the winning player the opportunity to enter the name and draw a congratulation message with the name over the board.

Tipps
If (probably on windows) the turtle-libary is not found by python3, save the following turtle.py-file in the same directory as your assignment file.
In turtle you are probably going to use 
movingTurtle.penup() 
movingTurtle.pendown()
movingTurtle.forward(length)
movingTurtle.setheading(dir)
movingTurtle.goto(x, y)
movingTurtle.circle(radius)
movingTurtle.write(text)
movingTurtle.color(color)
and others...
You have to be consistent with the padding in python. Ether use a tabulator, 2-, or 4-spaces.