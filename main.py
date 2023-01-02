import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

# Initialize scoreboard
sb = Scoreboard()

# Initialize player
dog = Player()
screen.onkey(dog.move, "Up")

game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()
    sb.display_level(dog.level)

    if dog.ycor() == FINISH_LINE_Y:
        dog.increase_level()

screen.exitonclick()
