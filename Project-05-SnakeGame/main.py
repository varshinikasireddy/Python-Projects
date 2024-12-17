from turtle import  Screen,Turtle

from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

border = Turtle()
border.color("white")
border.penup()
border.goto(-300, 300)  # Top-left corner
border.pendown()
border.pensize(3)  # Border thickness

for _ in range(4):  # Draw a square
    border.forward(600)  # Adjust size
    border.right(90)

border.hideturtle()

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.update()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        is_game_on=False
        scoreboard.game_over()
    for seg in snake.segments:
        if seg ==snake.head:
            pass
        elif snake.head.distance(seg)<10:
            is_game_on=False
            scoreboard.game_over()
screen.exitonclick()

