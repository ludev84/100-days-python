from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 36, 'bold')
SCREEN_HEIGHT = 600

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.computer_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(SCREEN_HEIGHT / 2 - 80)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.user_score}             {self.computer_score}", align=ALIGNMENT, font=FONT)

    def increase_user_score(self):
        self.user_score += 1
        self.update_scoreboard()

    def increase_computer_score(self):
        self.computer_score += 1
        self.update_scoreboard()