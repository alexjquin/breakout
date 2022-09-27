from turtle import *

from ball import Ball

HORIZONTAL = -260

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(1, 8, 1)

        self.goto(0, HORIZONTAL)

    def follow_mouse(self, event) -> None:
        x = event.x - 500

        self.goto(x, HORIZONTAL)

    def check_collision(self, ball: Ball) -> None:
        ball_xcor = ball.xcor()
        ball_ycor = ball.ycor()
        paddle_xcor = self.xcor()
        paddle_ycor = self.ycor()

        old_heading = ball.heading()
        new_heading = old_heading

        if paddle_ycor - 10 <= ball_ycor <= paddle_ycor + 10 and paddle_xcor - 80 <= ball_xcor <= paddle_xcor + 80\
                and 180 < old_heading < 360:
            # Bounce up
            if paddle_xcor - 79 < ball_xcor < paddle_xcor:
                new_heading = 90 + (paddle_xcor - ball_xcor) * (9/8)
            elif paddle_xcor < ball_xcor < paddle_xcor + 79:
                new_heading = 0 + (paddle_xcor + 80 - ball_xcor) * (9/8)
        ball.setheading(new_heading)