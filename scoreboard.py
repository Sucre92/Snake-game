from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 25, "normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}", align="center", font=("Arial", 25, "normal"))


