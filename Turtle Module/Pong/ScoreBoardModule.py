import turtle


class ScoreBoard:
    def __init__(self):
        super().__init__()
        self.tort = turtle.Turtle()
        self.tort.penup()
        self.tort.hideturtle()
        self.tort.color("white")
        self.tort.goto(2, 220)
        self.tort.write("0 : 0", font=("Arial", 24, "normal"), align="center")


    def Refresh(self, player_score, computer_score):
        self.tort.clear()
        self.tort.write(f"{player_score} : {computer_score}", font=("Arial", 24, "normal"), align="center")


def CreateLine():
    line = turtle.Turtle()
    line.hideturtle()
    line.color("white")
    line.left(90)

    for i in range(6):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)
    
    line.home()
    line.left(90)
    line.back(20)

    for i in range(6):
        line.pendown()
        line.back(20)
        line.penup()
        line.back(20)
