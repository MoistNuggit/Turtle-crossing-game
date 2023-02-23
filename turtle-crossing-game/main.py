import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player= Player()
cars = CarManager()
# cars.create_cars(5)
# screen.ontimer(cars.create_cars(5),1000)

screen.listen()
screen.onkeypress(fun=player.move_up, key="w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # screen.ontimer(cars.create_cars(5),1000)
    cars.create_cars()
    cars.move()

    # BELOW:DETECT WHEN PLAYER HAS CROSSED THE FINISH LINE AND GOES TO A NEW LEVEL
    if player.ycor() >= 280:
        player.sety(-280)
        scoreboard.new_level()
        cars.new_level()

    for car in cars.cars_list:
        if player.distance(car) <= 30 and player.ycor() - car.ycor() <=10:
            game_is_on = False
            print("Game Overwwwwww")
            scoreboard.game_over()
        elif player.distance(car) <= 30 and car.ycor() - player.ycor() <=10:
            game_is_on = False
            scoreboard.game_over()
            print("Game Over")


