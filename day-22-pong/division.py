from turtle import Turtle

SCREEN_HEIGHT = 600


class Division(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.pensize(width=5)
        self.goto(0, -(SCREEN_HEIGHT / 2))
        self.setheading(90)
        self.draw_division()

    def draw_division(self):
        for _ in range(int(-(SCREEN_HEIGHT / 2)), int((SCREEN_HEIGHT / 2) - 20), 20):
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(10)