from turtle import Screen, Turtle
from player import Player
from food import Food
from yellow_ghost import Yellow
from white_ghost import White
from pinky_ghost import Pink
from scoreboard import Scoreboard
from maze1.wall9 import Wall9
from maze1.wall1 import Wall1
from maze1.wall2 import Wall2
from maze1.wall3 import Wall3
from maze1.wall4 import Wall4
from maze1.wall5 import Wall5
from maze1.wall6 import Wall6
from maze1.wall7 import Wall7
from maze1.wall8 import Wall8
import time

turtle = Turtle

# Setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Triangle maze runner")
screen.tracer(0)

player = Player()
food = Food()
scoreboard = Scoreboard()
pinky = Pink()
white = White()
yellow = Yellow()

# Player Control
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.turn_left, "Left")
screen.onkeypress(player.turn_right, "Right")
screen.onkeypress(food.refresh, "f")

food.refresh()
difficulty = screen.textinput(title="Level", prompt="Easy;Normal;Hard;Extreme").lower()
player_name = screen.textinput(title="Player_name", prompt="What is your name.").lower()
minus_time = 0

if difficulty == "easy":
    minus_time = 0.00001
if difficulty == "easy":
    minus_time = 0.0001
elif difficulty == "normal":
    minus_time = 0.001
elif difficulty == "hard":
    minus_time = 0.01
elif difficulty == "extreme":
    minus_time = 0.01
else:
    print("Invalid!")

wall9 = Wall9()
wall1 = Wall1()
wall2 = Wall2()
wall3 = Wall3()
wall4 = Wall4()
wall5 = Wall5()
wall6 = Wall6()
wall7 = Wall7()
wall8 = Wall8()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(player.speed)
    player.move()
    wall9.create()
    wall1.create()
    wall2.create()
    wall3.create()
    wall4.create()
    wall5.create()
    wall6.create()
    wall7.create()
    wall8.create()
    yellow.create()
    white.create()
    pinky.create()
    yellow.move()
    pinky.move()
    white.move()

    # Detect collision with food.
    if player.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        player.speed -= minus_time

    # Detect if the food is in the wall.
    if food.distance(wall9) < 55 or food.distance(wall1) < 55 or food.distance(wall2) < 65 or player.distance(
            wall3) < 65 or food.distance(wall4) < 55 or food.distance(wall5) < 55 or food.distance(
        wall6) < 65 or food.distance(wall7) < 65 or food.distance(wall8) < 55:
        food.refresh()

    # Detect collision with wall.
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        scoreboard.game_over()

        again = screen.textinput(title="Again", prompt="Do you want to play again? Yes or no.").lower()
        if again == "yes":
            scoreboard.reset_player(player_name, difficulty)
            player.reset_p()
        elif again == "no":
            game_is_on = False

    # Detect collision with the maze.
    if player.distance(wall9) < 50 or player.distance(wall1) < 50 or player.distance(wall2) < 65 or player.distance(
            wall3) < 65 or player.distance(wall4) < 50 or player.distance(wall5) < 50 or player.distance(
        wall6) < 65 or player.distance(wall7) < 65 or player.distance(wall8) < 50:
        white.reset_ghost()
        yellow.reset_ghost()
        pinky.reset_ghost()
        scoreboard.game_over()

        again = screen.textinput(title="Again", prompt="Do you want to play again? Yes or no.").lower()
        if again == "yes":
            scoreboard.reset_player(player_name, difficulty)
            player.reset_p()
        elif again == "no":
            game_is_on = False

    # Detect collision with the triangle.
    if player.distance(white) < 15 or player.distance(yellow) < 15 or player.distance(pinky) < 15:
        white.reset_ghost()
        yellow.reset_ghost()
        pinky.reset_ghost()
        again = screen.textinput(title="Again", prompt="Do you want to play again? Yes or no.").lower()
        if again == "yes":
            scoreboard.reset_player(player_name, difficulty)
            player.reset_p()
        elif again == "no":
            game_is_on = False

    # Yellow AI
    if yellow.is_close(player):
        if player.xcor() < yellow.xcor():
            yellow.turn_left()
        elif player.xcor() > yellow.xcor():
            yellow.turn_right()
        elif player.ycor() < yellow.ycor():
            yellow.down()
        elif player.ycor() > yellow.ycor():
            yellow.up()
    if yellow.distance(wall9) < 50 or yellow.distance(wall1) < 50 or yellow.distance(wall2) < 65 or yellow.distance(
            wall3) < 65 or yellow.distance(wall4) < 50 or yellow.distance(wall5) < 50 or yellow.distance(
        wall6) < 65 or yellow.distance(wall7) < 65 or yellow.distance(
        wall8) < 50 or yellow.xcor() > 290 or yellow.xcor() < -290 or yellow.ycor() > 290 or yellow.ycor() < -290:
        yellow.random_turn()

    if player.heading() == 90:
        pinky.setheading(90)
    elif player.heading() == 0:
        pinky.setheading(0)
    elif player.heading() == 180:
        pinky.setheading(180)
    elif player.heading() == 270:
        pinky.setheading(270)

    if player.heading() == 90:
        white.setheading(270)
    elif player.heading() == 0:
        white.setheading(180)
    elif player.heading() == 180:
        white.setheading(0)
    elif player.heading() == 270:
        white.setheading(90)

screen.exitonclick()
