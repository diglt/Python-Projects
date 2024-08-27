import turtle

Screen = turtle.Screen()

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
            
        self.goto(0, 250)
        self.write("Current score is: 0", font=("Arial", 24, "normal"), align="center")
    
    def Refresh(self, score):
        self.clear()
        self.goto(0, 200)
        self.write(f"Current score is: {score}", font=("Arial", 24, "normal"), align="center")

