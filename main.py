import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

# Initialize player
dog = Player()
screen.onkey(dog.move, "Up")

game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
