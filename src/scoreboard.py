from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
GAMEOVERFONT = ("Courier", 48, "normal")

class Scoreboard(Turtle):
    """This class is responsible for level management."""
    def __init__(self):
        """Init level on the screen."""
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-200.00, 265.00)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font = FONT)
    
    def increase_level(self):
        """This method increases current level."""
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font = FONT)

    def game_over(self):
        """This method prints ending text on the screen."""
        self.clear()
        self.goto(0.00, 0.00)
        self.write(f"GAME OVER", align = "center", font = GAMEOVERFONT)