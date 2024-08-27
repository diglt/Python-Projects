import turtle
import random

Screen = turtle.Screen()

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(2, 2)
        self.Refresh()  
    
    def Refresh(self):
        x = random.randint(-500 + 20, 500 -20)
        y = random.randint(-300 + 20, 300 -20)
        self.goto(x, y)
