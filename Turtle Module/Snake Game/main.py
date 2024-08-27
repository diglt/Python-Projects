import turtle
import time
import random
import SnakeModule
import FoodModule
import ScoreBoard

the_screen = turtle.Screen()
the_screen.bgcolor("black")
the_screen.colormode(255)
the_screen.tracer(0)
the_screen.setup(width=1000, height=600)
the_screen.bgcolor("white")

the_food = FoodModule.Food()

snake = SnakeModule.Snake()
snake_parts = snake.SnakeParts
snake_head = snake_parts[0]

Score = 0
score_board = ScoreBoard.ScoreBoard()

def MoveLeft():
    snake_head.left(90)

def MoveRight():
    snake_head.right(90)

def AddNewPart(snake):
    new_part = turtle.Turtle()
    new_part.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    new_part.shape("square")
    new_part.penup()

    position = snake.SnakeParts[-1].position()  
    new_part.goto(position)  

    snake.SnakeParts.append(new_part)

def GameOver():
    game_over = turtle.Turtle()
    game_over.penup()
    game_over.goto(0, 0)
    game_over.color("black")
    game_over.write("Game over.", font=("Arial", 24, "normal"), align="center")

IsRunning = True
while IsRunning:
    the_screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_parts) - 1, 0, -1):
        new_x = snake_parts[seg_num - 1].xcor()
        new_y = snake_parts[seg_num - 1].ycor()
        snake_parts[seg_num].goto(new_x, new_y)

    snake_head.forward(20)

    if snake_head.distance(the_food) < 15:
        print("Food eaten!")
        the_food.Refresh()

        Score += 1
        score_board.Refresh(Score)

        AddNewPart(snake)

    if snake_head.xcor() > 465 or snake_head.xcor() < -465 or snake_head.ycor() > 300 or snake_head.ycor() < -300:
        IsRunning = False
        GameOver()

    if len(snake_parts) > 3:
        for snake_segment in snake_parts[1:]:
            if snake_head.distance(snake_segment) < 10:
                IsRunning = False
                GameOver()


    the_screen.listen()
    the_screen.onkey(fun=MoveLeft, key="w")
    the_screen.onkey(fun=MoveLeft, key="a")
    the_screen.onkey(fun=MoveRight, key="s")
    the_screen.onkey(fun=MoveRight, key="d")

the_screen.exitonclick()
