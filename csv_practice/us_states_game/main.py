import turtle
import pandas
import sys


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)

turtle.shape(image)

states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name?")
    # print(answer_state)

    if answer_state == "exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print("The missing states list has been saved to a csv file.")
        sys.exit()

    answer_state = answer_state.title()

    if answer_state in states_list:
        # print(answer_state)
        # initialise a turtle
        t = turtle.Turtle()
        t.hideturtle()
        # penup so that it doesn't draw anything
        t.penup()
        # get the corresponding row of the state
        state_data = data[data.state == answer_state]
        coordinates = state_data.iloc[0].to_list()
        # list index 1 is x-coordinate and list index 2 is y-coordinate

        # go to the location of the state
        t.goto(coordinates[1], coordinates[2])
        t.write(coordinates[0])

        guessed_states.append(answer_state)


screen.exitonclick()

"""
To get the coordinates of a point on the turtle window we just have to click on that point

uncomment the code below to use this function
"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
