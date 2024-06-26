from turtle import Turtle

MOVE_PAD = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ComputerPad(Turtle):
    def __init__(self):
        super().__init__()
        self.direction = "up"
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.goto(SCREEN_WIDTH / 2 - 30, 0)

    def move(self):
        if self.direction == "down":
            self.backward(MOVE_PAD)
        if self.direction == 'up':
            self.forward(MOVE_PAD)

        if self.ycor() < -(SCREEN_HEIGHT / 2 - 60):
            self.direction = "up"
        if self.ycor() > SCREEN_HEIGHT / 2 - 60:
            self.direction = "down"