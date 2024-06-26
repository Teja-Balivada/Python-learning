import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to Turtle Race!")
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ycord = -100

all_turtles = []

for turtle_index in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    ycord += 25
    new_turtle.goto(x= -230, y=ycord)
    all_turtles.append(new_turtle)

if user_bet:
     is_race_on = True

while is_race_on:
     
     for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()