from turtle import Turtle

MOVE_PAD = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class UserPad(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.goto(-(SCREEN_WIDTH / 2) + 30, 0)

    def up(self):
        if self.ycor() < SCREEN_HEIGHT / 2 - 40:
            self.forward(MOVE_PAD)

    def down(self):
        if self.ycor() > -(SCREEN_HEIGHT / 2 - 40):
            self.backward(MOVE_PAD)