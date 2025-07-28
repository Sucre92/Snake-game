import  time
from snake import Snake
from turtle import Screen,Turtle
from food import Food
from scoreboard import Scoreboard
from tkinter import messagebox
from snake import pygame

snake= Snake()
food=Food()
screen = Screen()
scoreboard=Scoreboard()

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on= True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # for playing snake.mp3 file


    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() < -280 or snake.head.xcor()> 280 \
            or snake.head.ycor() <-280 or snake.head.ycor()>280:
        is_game_on=False
        messagebox.showinfo("GAME OVER: You lose")
        snake.hiss_sound().pause()
        screen.bye()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)==segment:
            is_game_on=False
            snake.hiss_sound().pause()
            messagebox.showinfo("You bit your tail!")
            screen.bye()
    snake.hiss_sound()


screen.exitonclick()