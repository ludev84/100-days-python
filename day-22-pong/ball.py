from turtle import Turtle

MOVE_BALL = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.x_direction = "left"
        self.y_direction = "up"
        self.shape("circle")
        self.color("white")
        self.penup()

    def re_set(self):
        # self.goto(1000, 1000)
        self.reset()
        self.create_ball()

    def move(self):
        xcor = self.xcor()
        ycor = self.ycor()
        if ycor > SCREEN_HEIGHT / 2 - 20:
            self.y_direction = "down"
        if ycor < -(SCREEN_HEIGHT / 2 - 20):
            self.y_direction = "up"

        if self.x_direction == "left":
            self.setx(xcor - MOVE_BALL)
        else:
            self.setx(xcor + MOVE_BALL)

        if self.y_direction == "up":
            self.sety(ycor + MOVE_BALL)
        else:
            self.sety(ycor - MOVE_BALL)