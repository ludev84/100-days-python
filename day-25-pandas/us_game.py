import turtle
import pandas

ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
screen.tracer(0)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

game_is_on = True

while game_is_on:
    screen.update()
    answer_state = screen.textinput(title=f"{abs(len(states_list) - 50)}/50 states guessed",
                                    prompt="What's another state's name?").title()
    state = data[data.state == answer_state]
    if answer_state == "Exit":
        states_to_learn = pandas.DataFrame(states_list)
        states_to_learn.to_csv("states_to_learn.csv")
        game_is_on = False
    if len(state) > 0:
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(state.x.iloc[0], state.y.iloc[0])
        text.write(state.state.iloc[0])
        states_list.remove(state.state.iloc[0])
    if len(states_list) == 0:
        game_is_on = False

screen.exitonclick()
