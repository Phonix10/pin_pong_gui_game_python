from turtle import *

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1,1)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_sp = 0.1

    def move(self):
        nx = self.xcor() + self.x_move
        ny = self.ycor() + self.y_move
        self.goto(nx,ny)

    def bounce(self):
        self.y_move = self.y_move * (-1)


    def bounce_paddle(self):
        self.x_move = self.x_move * (-0.5)
        self.x_move *= 1

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_paddle()
        self.move_sp = 0.1

