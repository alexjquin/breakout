from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.lives = 3
        self.score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.print_score()

    def brick_hit(self):
        self.score += 10
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Lives: {self.lives}     Score: {self.score}",
                   align="center", font=("Arial", 20, "normal"))

    def lose_life(self):
        self.lives -= 1
        self.print_score()

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.pendown()
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
