from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
r_paddle = Paddle()
r_paddle.goto(350, 0)
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
l_paddle = Paddle()
l_paddle.goto(-350, 0)
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
scoreboard_right = Scoreboard()
scoreboard_right.goto(100, 250)
scoreboard_right.right_score()

scoreboard_left = Scoreboard()
scoreboard_left.goto(-100, 250)
scoreboard_left.left_score()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() >320 and ball.distance(r_paddle) < 50 or ball.xcor() <-320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball.ball_speed *= 0.90
    if ball.xcor() > 360 or ball.xcor()<-360:
        if ball.xcor() > 360:
            scoreboard_left.left_updated_score()
        if ball.xcor() < -360:
            scoreboard_right.right_updated_score()
        ball.goto(0,0)
        ball.ball_reverse()
        ball.ball_speed = 0.1
    screen.update()

screen.exitonclick()