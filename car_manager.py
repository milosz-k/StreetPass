from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    """This class is responsible for cars which are passing the road managment."""
    def __init__(self) -> None:
        super().__init__()
        self.block = []
        self.create_car()
    
    def create_car(self) -> None:
        """This method creates new 2x1 block sized car and turns it to the left."""
        for new_part in range(2):
            new_part = Turtle("square")
            new_part.penup()
            self.block.append(new_part)
        self.block[0].color(random.choice(COLORS))
        self.block[0].setposition(300, random.randint(-250, 250))
        self.block[1].color(self.block[0].pencolor())
        self.block[1].setposition(self.block[0].xcor() + 20, self.block[0].ycor())
        self.block[0].right(180)
        self.block[1].right(180)
    
    def move(self, speed) -> None:
        """This method assigns speed value to the car."""
        for part in self.block:
            part.forward(STARTING_MOVE_DISTANCE + speed * MOVE_INCREMENT)

    
