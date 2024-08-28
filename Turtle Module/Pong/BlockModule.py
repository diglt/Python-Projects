import turtle
import random

class BlockPart:
    def __init__(self) -> None:
        self.block = turtle.Turtle()
        self.block.shape("square")
        self.block.shapesize(5, 1)
        self.block.penup()
        self.block.color("white")
        self.block.goto(-475, 0)

class ComputerPart:
    def __init__(self):
        self.part = turtle.Turtle()
        self.part.shape("square")
        self.part.shapesize(5, 1)
        self.part.penup()
        self.part.color("white")
        self.part.goto(475, 0)


    def MoveTowardsBall(self, ball_ycor):
        current_y = self.part.ycor()
        new_y = current_y + (ball_ycor - current_y) * 0.1
        self.part.sety(new_y)
        


class PongBall:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.shapesize(1)
        self.ball.penup()
        self.ball.color("white")
        self.dx = 5
        self.dy = 5

    def Begin(self):
        self.ball.goto(-475, 0)
