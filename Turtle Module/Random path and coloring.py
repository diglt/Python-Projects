import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

Window = Screen()

Window.bgcolor("black")

pet_turtle = Turtle()

colors = ["red", "blue", "yellow", "green", "purple", "orange", "pink"]

pet_turtle.left(90)

pet_turtle.pensize(15)
pet_turtle.speed("fast")

def RandomRGB():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return R, G, B


for _ in range(300):
    pet_turtle.color(RandomRGB())
    pet_turtle.forward(30)
    pet_turtle.setheading(random.choice([0, 90, 180, 270]))


Window.exitonclick()
