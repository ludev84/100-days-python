import time
from turtle import Screen
from division import Division
from user_pad import UserPad
from computer_pad import ComputerPad

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

Division()
user_pad = UserPad()
computer_pad = ComputerPad()

screen.listen()
screen.onkeypress(user_pad.up, "Up")
screen.onkeypress(user_pad.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    computer_pad.move()



screen.exitonclick()