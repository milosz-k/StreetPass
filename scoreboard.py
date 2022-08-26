from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
GAMEOVERFONT = ("Courier", 48, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-200.00, 265.00)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font = FONT)
    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font = FONT)

    def game_over(self):
        self.clear()
        self.goto(0.00, 0.00)
        self.write(f"GAME OVER", align = "center", font = GAMEOVERFONT)