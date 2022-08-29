from turtle import Turtle
from xmlrpc.client import Boolean
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """This class is responsible for protagonist management."""
    def __init__(self) -> None:
        """Init protagonist."""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(STARTING_POSITION)

    def move(self) -> None:
        """This method makes protagonist move by predefined step."""
        self.forward(MOVE_DISTANCE)

    def reborn(self) -> Boolean:
        """This method relocates protagonist to the beggining after completing a level."""
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True #return celem dodania punktu