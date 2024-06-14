from turtle import *
from paddle import *
from ball import *
from scoreboard import *
import time


sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("green")
sc.title("PONG GAME")
sc.tracer(0)
game_on = True

pad_r = Paddle(350,0)
pad_l = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(pad_r.go_up, "Up")
sc.onkey(pad_r.go_Down, "Down")
sc.onkey(pad_l.go_up, "w")
sc.onkey(pad_l.go_Down, "s")


while game_on:
    time.sleep(0.0058)
    ball.move()
    sc.update()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.distance(pad_r) < 50 and ball.xcor() > 320 or ball.distance(pad_l) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.left_point()

    if ball.xcor() < (-380):
        ball.reset_pos()
        scoreboard.right_point()
    if scoreboard.left_sc ==10 or scoreboard.right_sc == 10:
        scoreboard.sc_last()
        game_on = False



sc.exitonclick()
