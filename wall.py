from ball import Ball
from turtle import *


COLORS = ["#4C0033", "#790252", "#AF0171", "#E80F88"]


class Wall:
    def __init__(self):
        self.wall = []
        self.build_wall()

    class Brick(Turtle):
        def __init__(self, brick_color, x, y):
            super().__init__()

            self.shape("square")
            self.color("black", brick_color)
            self.penup()
            self.turtlesize(2, 4, 1)

            self.goto(x, y)

    def build_wall(self):
        y = 100
        for row in range(0, 4):
            if row in [0, 2]:
                x = -500
            else:
                x = -460
            while x < 540:
                brick = self.Brick(COLORS[row], x, y)
                self.wall.append(brick)
                x += 80

            y -= 40

    def check_collision(self, ball: Ball) -> bool:
        old_heading = ball.heading()
        new_heading = old_heading
        bounce = False

        ball_xcor = ball.xcor()
        ball_ycor = ball.ycor()

        for brick in self.wall:
            brick_xcor = brick.xcor()
            brick_ycor = brick.ycor()

            if brick_xcor - 50 < ball_xcor < brick_xcor - 40 and brick_ycor - 30 < ball_ycor < brick_ycor + 30\
                    and (0 < old_heading < 90 or 270 < old_heading < 360):
                # Bounce left
                if 0 < old_heading < 90:
                    new_heading = 90 + (90 - old_heading)
                elif 270 < old_heading < 360:
                    new_heading = 270 - (old_heading - 270)
                bounce = True
                self.wall.remove(brick)
                brick.color("black")
            elif brick_xcor + 40 < ball_xcor < brick_xcor + 50 and brick_ycor - 30 < ball_ycor < brick_ycor + 30\
                    and 90 < old_heading < 270:
                # Bounce right
                if 90 < old_heading < 180:
                    new_heading = 90 - (old_heading - 90)
                elif 180 < old_heading < 270:
                    new_heading = 270 + (270 - old_heading)
                bounce = True
                self.wall.remove(brick)
                brick.color("black")
            elif brick_ycor - 30 < ball_ycor < brick_ycor - 20 and brick_xcor - 50 < ball_xcor < brick_xcor + 50\
                    and 0 < old_heading < 180:
                # Bounce down
                if 0 < old_heading <= 90:
                    new_heading = 360 - (old_heading - 0)
                elif 90 < old_heading < 180:
                    new_heading = 180 + (180 - old_heading)
                bounce = True
                self.wall.remove(brick)
                brick.color("black")
            elif brick_ycor + 20 < ball_ycor < brick_ycor + 30 and brick_xcor - 50 < ball_xcor < brick_xcor + 50\
                    and 180 < old_heading < 360:
                # Bounce up
                if 180 < old_heading <= 270:
                    new_heading = 180 - (old_heading - 180)
                elif 270 < old_heading < 360:
                    new_heading = 0 + (360 - old_heading)
                bounce = True
                self.wall.remove(brick)
                brick.color("black")


        ball.setheading(new_heading)
        return bounce

    def empty(self) -> bool:
        return len(self.wall) == 0
