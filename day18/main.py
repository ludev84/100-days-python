import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
# tim.pensize(5)
screen = t.Screen()

directions = [0, 90, 180, 270]

palette = [(215, 168, 77), (80, 110, 151), (116, 159, 205), (242, 224, 235), (105, 173, 136),
       (190, 122, 159), (69, 126, 96), (127, 24, 63), (154, 50, 82), (162, 160, 54), (195, 78, 114),
       (218, 203, 125)]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.penup()
tim.hideturtle()
tim.goto(-400, -300)
# tim.dot(20, random.choice(palette))

for _ in range(10):
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(palette))
    xcor = tim.xcor()
    ycor = tim.ycor()
    tim.goto(xcor - 500, ycor + 50)

# size = 5
# for _ in range(int(360 / size)):
#     tim.pencolor(random_color())
#     tim.circle(100)
#     tim.left(size)

# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)

# figure_sides = 3
# for figure in range(8):
#     tim.pencolor(colors[figure])
#     for _ in range(figure_sides):
#         tim.forward(100)
#         tim.right(360/figure_sides)
#     figure_sides += 1
screen.exitonclick()
