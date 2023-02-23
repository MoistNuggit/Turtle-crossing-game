FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 0
        self.goto(-220,260)
        self.write(f"level: {self.level}", False, align="center", font=FONT)

    def new_level(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", False, align="center", font = FONT)


