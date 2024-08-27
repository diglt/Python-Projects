import turtle
import random

turtle.Screen().colormode(255)

class Snake:
    def __init__(self) -> None:
        self.SnakeParts = []
        
        for i in range(3):
            my_turtle = turtle.Turtle()
            my_turtle.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            my_turtle.shape("square")
            my_turtle.penup()

            position = -25 * i  # Negative to spread out to the left
            new_position = position, 0

            my_turtle.goto(new_position)

            self.SnakeParts.append(my_turtle)
