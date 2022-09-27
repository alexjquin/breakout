from turtle import *
import random


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()

        self.speed = speed
        self.moving = False

        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -220)

        initial_heading = random.randrange(45, 135, 1)
        self.setheading(initial_heading)

    def start(self):
        self.moving = True

    def move(self):
        if self.moving:
            self.forward(self.speed)

    def check_side_collision(self):
        old_heading = self.heading()
        new_heading = old_heading

        if self.xcor() < -490:
            if 90 < self.heading() < 180:
                new_heading = 90 - (old_heading - 90)
            elif 180 < self.heading() < 270:
                new_heading = 270 + (270 - old_heading)
        elif self.xcor() > 490:
            if 0 < old_heading < 90:
                new_heading = 90 + (90 - old_heading)
            elif 270 < old_heading < 360:
                new_heading = 270 - (old_heading - 270)

        self.setheading(new_heading)

    def check_bottom_collision(self):
        if self.ycor() < -290:
            return True

    def check_top_collision(self):
        old_heading = self.heading()
        new_heading = old_heading

        if self.ycor() > 290:
            if 0 < old_heading <= 90:
                new_heading = 360 - (old_heading - 0)
            elif 90 < old_heading < 180:
                new_heading = 180 + (180 - old_heading)

        self.setheading(new_heading)
