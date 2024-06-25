from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color").lower()
is_race_on = False


colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

start_x = -230
start_y = -120
count_color = 0

turtles = [Turtle(shape="turtle") for _ in range(7)]

for turtle in turtles:
    turtle.color(colors[count_color])
    turtle.penup()
    turtle.goto(start_x, start_y)
    count_color += 1
    start_y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
