from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.left_sc = 0
        self.right_sc = 0
        self.sc_update()


    def left_point(self):
        self.left_sc = self.left_sc + 1
        self.clear()
        self.sc_update()

    def right_point(self):
        self.right_sc = self.right_sc + 1
        self.clear()
        self.sc_update()

    def sc_update(self):
        self.goto((-100, 200))
        self.write(self.left_sc, align="center", font=("Courier", 80, "normal"))
        self.goto((100, 200))
        self.write(self.right_sc, align="center", font=("Courier", 80, "normal"))

    def sc_last(self):
        if self.left_sc == 10:
            self.goto(0,0)
            self.write(f"Left player win", align="center", font=("Courier", 40, "normal"))
        elif self.right_sc == 10:
            self.goto(0, 0)
            self.write(f"Right player win", align="center", font=("Courier", 40, "normal"))
