import turtle
import random

my_screen = turtle.Screen()
screen_width = 1000
screen_length = 400

my_screen.setup(width=screen_width, height=screen_length)
turtle.colormode(255)

turtles = []
colors = ["red", "blue", "green", "orange", "yellow"]

IsRunning = True


def CreateTurtles():
    for i in range(5):
        position = 25 * i
        random_color = colors[i]

        turtle_string = turtle.Turtle()
        turtle_string.penup()
        turtle_string.shape("turtle")

        turtle_string.color(random_color)

        turtle_string.goto(-225, position)
        turtles.append(turtle_string)


def CheckWinner(turtle_color):
    if turtle_color == chosen_bet:
        print("Congratulations, you win!")
    else:
        print(f"Your guess was wrong, {turtle_color} won!")


def MoveTurtles():
    global IsRunning
    
    for turtle in turtles:
        if turtle.pos()[0] < screen_width / 2:
            random_distance = random.randint(5, 25)

            turtle.forward(random_distance)
        else:
            winner_color = turtle.color()

            CheckWinner(winner_color[0])
            my_screen.bye()

            IsRunning = False
            break


chosen_bet = my_screen.textinput("Make your bet!", "Which turtle will win the race? ")
CreateTurtles()

while IsRunning:
    MoveTurtles()
