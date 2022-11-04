from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Kyle's Pong Game")
screen.tracer(0)
scoreboard = Score()
sleep_time = 0.05


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()


screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    print(l_paddle.pos())
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    if ball.xcor() < l_paddle.xcor()+20:
        if l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50:
            ball.paddle_bounce()
            sleep_time *= .8
        else:
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            time.sleep(3)
            sleep_time = 0.05
            ball.respawn()

    if ball.xcor() > r_paddle.xcor()-20:
        if r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50:
            ball.paddle_bounce()
            sleep_time *= .8
        else:
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            time.sleep(3)
            sleep_time = 0.05
            ball.respawn()


screen.exitonclick()

