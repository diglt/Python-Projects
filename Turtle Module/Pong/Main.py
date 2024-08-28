import turtle
import random
import ScoreBoardModule, BlockModule

score_to_reach = 5
player_score = 0
computer_score = 0

Screen = turtle.Screen()
Screen.bgcolor("black")
Screen.setup(1000, 500)

ScoreBoard = ScoreBoardModule.ScoreBoard()

PongBall = BlockModule.PongBall()
Player = BlockModule.BlockPart()
Computer = BlockModule.ComputerPart()

ScoreBoardModule.CreateLine()
PongBall.Begin()


def MoveUp():
    new_Y = Player.block.ycor() + 25
    Player.block.sety(new_Y)


def MoveDown():
    new_Y = Player.block.ycor() - 25
    Player.block.sety(new_Y)


def MoveBall():
    global player_score, computer_score  # python and the scope of a function being local or global is odd man
    PongBall.ball.setx(PongBall.ball.xcor() + PongBall.dx)
    PongBall.ball.sety(PongBall.ball.ycor() + PongBall.dy)

    if PongBall.ball.ycor() > 240 or PongBall.ball.ycor() < -240:
        PongBall.dy *= -1

    if PongBall.ball.distance(Player.block) < 50 and PongBall.ball.xcor() < -450: # player
        PongBall.dx *= -1

    if PongBall.ball.distance(Computer.part) < 50 and PongBall.ball.xcor() > 450: # computer
        PongBall.dx *= -1

    if PongBall.ball.xcor() > 490:
        PongBall.ball.goto(0, 0)
        PongBall.dx *= -1

        computer_score += 1
        ScoreBoard.Refresh(player_score, computer_score)

    if PongBall.ball.xcor() < -490:
        PongBall.ball.goto(0, 0)
        PongBall.dx *= -1

        player_score += 1
        ScoreBoard.Refresh(player_score, computer_score)


def GameLoop():
    MoveBall()
    Computer.MoveTowardsBall(PongBall.ball.ycor())

    Screen.listen()
    Screen.onkey(fun=MoveUp, key="w")
    Screen.onkey(fun=MoveDown, key="s")

    Screen.update()
    Screen.ontimer(GameLoop, 20)


Screen.tracer(0)
GameLoop()
Screen.mainloop()
