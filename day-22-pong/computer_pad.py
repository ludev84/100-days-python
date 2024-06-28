from turtle import Turtle

MOVE_PAD = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ComputerPad(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        # self.setheading(90)
        self.goto(SCREEN_WIDTH / 2 - 30, 0)

    def up(self):
        if self.ycor() < SCREEN_HEIGHT / 2 - 40:
            self.sety(self.ycor() + MOVE_PAD)

    def down(self):
        if self.ycor() > -(SCREEN_HEIGHT / 2 - 40):
            self.sety(self.ycor() - MOVE_PAD)