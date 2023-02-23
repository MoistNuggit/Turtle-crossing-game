COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0
# INCREASE MOVE_INCREMENT BY 10 EVERY LEVEL
from turtle import Turtle
import random
import threading

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list =[]
        self.penup()
        self.hideturtle()
        self.move_increment = 0
        self.car_gen_chance = 10

    def create_cars(self):
        # THE RANDOM PART BELOW IS BECAUSE IN MAIN SCREEN SLEEPS FOR 0.1 SECOND SO IF ON EVERY
        # REFRESH OF THE SLEEP A NEW CAR GENERAES IT'D BE IMPOSSIBLE,
        # SO NOW THERES ONLY A CERTAIN CHANCE A CAR APPEARS
        if random.randint(1,10) == 1:
            new_car =Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(x=300, y= random.randint(-240,280))
            self.cars_list.append(new_car)

    def move(self):
        for car in self.cars_list:
            new_x_cor = car.xcor() - STARTING_MOVE_DISTANCE - self.move_increment
            car.setx(new_x_cor)

    def new_level(self):
        # for car in self.cars_list:
        #     car.clear()
        # self.cars_list.clear()
        self.move_increment += 10
        if self.car_gen_chance >=1:
            self.car_gen_chance -= 3

    # def create_cars(self):
    #     threading.Timer(1.0,self.create_cars()).start()
    #     for i in range(5):
    #         new_car =Turtle(shape="square")
    #
    #         new_car.color(random.choice(COLORS))
    #         new_car.turtlesize(stretch_wid=1, stretch_len=3)
    #         new_car.penup()
    #         new_car.goto(x=300, y= random.randint(-280,280))
    #         self.cars_list.append(new_car)


    
