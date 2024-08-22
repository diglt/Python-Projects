import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

Window = Screen()

Window.bgcolor("black")

pet_turtle = Turtle()

pet_turtle.left(90)

pet_turtle.pensize(2)
pet_turtle.speed(0)

def RandomRGB():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return R, G, B

tilt = 0

for _ in range(300):
    pet_turtle.left(tilt)
    pet_turtle.color(RandomRGB())
    pet_turtle.circle(130)
    pet_turtle.home()
    tilt += 5


Window.exitonclick()
