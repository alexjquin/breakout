import time
import turtle
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from wall import Wall

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

ball_speed = 3


def start_ball(event):
    ball.start()


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
wall = Wall()
paddle = Paddle()
ball = Ball(ball_speed)

canvas = turtle.getcanvas()
canvas.bind('<Motion>', paddle.follow_mouse)
canvas.bind("<Button-1>", start_ball)

game_is_on = True
screen.update()

while game_is_on:
    screen.update()

    ball.move()

    if wall.check_collision(ball):
        scoreboard.brick_hit()

    paddle.check_collision(ball)

    ball.check_side_collision()
    ball.check_top_collision()

    if ball.check_bottom_collision():
        scoreboard.lose_life()
        ball.color("black")
        ball = Ball(ball_speed)
        if scoreboard.lives == 0:
            game_is_on = False

    if wall.empty():
        ball_speed += 3
        wall = Wall()
        ball = Ball(ball_speed)

scoreboard.game_over()

screen.mainloop()
