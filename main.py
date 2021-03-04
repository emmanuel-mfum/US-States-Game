import turtle
import pandas
import time

FONT = ("Arial", 16, "normal")


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
writer = turtle.Turtle()  # creates a Turtle whose purpose is to write the states on the map
writer.hideturtle()
writer.penup()
result = turtle.Turtle()  # creates a Turtle whose purpose is to write if the guess is incorrect or the game done
result.hideturtle()
result.penup()

screen.addshape(image)  # install the image to the screen
turtle.shape(image)  # set turtle shape

game_is_on = True

data = pandas.read_csv("50_states.csv")  # get the whole data from the csv file
states = data["state"].to_list()  # convert the column of data under "state" into a list
correct_states = []  # list of all the correctly guessed states
score = 0  # initial score


while game_is_on:  # a loop to keep the user guessing until the game is done
    # Convert guess in title case
    if score == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name").title()

    else:
        answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missed_states = []  # create empty list for the states missed by the user
        for state in states:  # compare the guessed states with the whole list of states
            if state not in correct_states:
                missed_states.append(state)

        new_data = pandas.DataFrame(missed_states)  # create a data frame with the list missed_states
        new_data.to_csv("states_to_learn.csv")  # create a csv file

        break

    # Check to see if the guess is among the 50 states
    if answer_state in states:
        current_state = data[data.state == answer_state]
        x_state = int(current_state.x)
        y_state = int(current_state.y)

        #  Write the correct guess on the map
        if answer_state not in correct_states:
            writer.goto(x_state, y_state)
            writer.pendown()
            writer.write(answer_state)
            writer.penup()
            correct_states.append(answer_state)  # record correct guesses in a loop
            score += 1  # updates the score

            if score == 50:
                game_is_on = False
                result.pendown()
                result.color("green")
                result.write("Well done ! You guessed all the states correctly", align="center", font=FONT)
                time.sleep(2)
                result.penup()

        else:
            result.goto(0, 0)
            result.pendown()
            result.color("green")
            result.write("Already guessed !", align="center", font=FONT)
            time.sleep(1)
            result.penup()
            result.clear()

    else:
        result.goto(0, 0)
        result.pendown()
        result.color("red")
        result.write("Incorrect guess !", font=FONT)
        time.sleep(1)
        result.penup()
        result.clear()

# states to learn

