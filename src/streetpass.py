import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

CAR_RESP_FREQUENCE = 6
CAR_RESP = 0

man = Player()
score = Scoreboard()

cars = []
game_is_on = True
speed_lvl = 0
while game_is_on:
    time.sleep(0.05)
    screen.update()
    screen.onkey(key="Up", fun=man.move)
    if CAR_RESP % CAR_RESP_FREQUENCE == 0:
        new_car = CarManager()
        cars.append(new_car)
    for auto in cars:
        auto.move(speed_lvl)
        if auto.block[0].distance(man) <= 20:
            score.game_over()
            game_is_on = False
    CAR_RESP += 1
    if man.ycor() > 290:
        man.reborn()
        score.increase_level()
        speed_lvl += 1
    
screen.exitonclick()