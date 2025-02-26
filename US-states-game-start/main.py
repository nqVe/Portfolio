import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
list_of_states = states.state.to_list()
correct_states = 0
all_states = []

while len(all_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State, {correct_states}/50 States correct",
                                    prompt="What is next State's name that you remember?").title()
    state_data_row = states[states.state == answer_state]
    if answer_state == "Exit":
        states_to_learn_list = [states for states in list_of_states if states not in all_states]
        break

    if list_of_states.__contains__(answer_state):
        all_states.append(answer_state)
        answer = turtle.Turtle()
        answer.penup()
        answer.ht()
        answer.goto(state_data_row.x.item(), state_data_row.y.item())
        answer.write(state_data_row.state.item(), align="center", font=("Arial", 8, "normal"))
        screen.title(f"{correct_states}/50")
        correct_states += 1

print(states_to_learn_list)
states_to_learn = pandas.DataFrame(states_to_learn_list)
states_to_learn.to_csv("States_to_learn")
