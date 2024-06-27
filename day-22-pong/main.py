import time
from turtle import Screen
from division import Division
from user_pad import UserPad
from computer_pad import ComputerPad
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

Division()
user_pad = UserPad()
computer_pad = ComputerPad()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(user_pad.up, "Up")
screen.onkeypress(user_pad.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    computer_pad.move()

    # Detect contact with pads
    if user_pad.distance(ball) < 30:
        ball.x_direction = "right"
    if computer_pad.distance(ball) < 30:
        ball.x_direction = "left"

    # Ball out of boundaries (score)
    if ball.xcor() < -(SCREEN_WIDTH / 2):
        scoreboard.increase_computer_score()
        ball.re_set()
    if ball.xcor() > SCREEN_WIDTH / 2:
        scoreboard.increase_user_score()
        ball.re_set()


screen.exitonclick()