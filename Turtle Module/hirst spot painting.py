import random
import turtle
import colorgram
from turtle import Turtle, Screen

color_palette = colorgram.extract(r'C:\Users\URUSERHERE\Downloads\IMAGELOCATION.jpeg', 10)

rgb_colors = []

for i in range(0,10):
    color_tuple = tuple(color_palette[i].rgb)
    rgb_colors.append(color_tuple)



turtle.colormode(255)

Window = Screen()

Window.bgcolor("black")

pet_turtle = Turtle()

pet_turtle.pensize(2)
pet_turtle.pensize(20)
pet_turtle.speed(0)
pet_turtle.hideturtle()

index = 1


while index < 10:
    forward_amount = 50 * index

    for i in range(10):
        random_tuple = rgb_colors[random.randint(1, (len(rgb_colors) - 1))]

        pet_turtle.color(random_tuple)
        pet_turtle.pendown()
        pet_turtle.forward(1)

        pet_turtle.penup()
        pet_turtle.forward(50)
    
    pet_turtle.home()
    pet_turtle.left(90)
    pet_turtle.forward(forward_amount)
    pet_turtle.right(90)
    index += 1

    

Window.exitonclick()
