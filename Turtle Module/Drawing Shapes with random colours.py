import random
from turtle import Turtle, Screen

Window = Screen()

pet_turtle = Turtle()

colors = ["red", "blue", "yellow", "green", "purple", "orange", "pink"]

index = 3

while index < 10:
    list_index = random.randint(0, (len(colors) - 1))
    print(list_index)
    pet_turtle.color(colors[list_index])

    new_turn = 360 / index
    for i in range(0,   index):
        pet_turtle.left(new_turn)
        pet_turtle.forward(100)
    index += 1

Window.exitonclick()
