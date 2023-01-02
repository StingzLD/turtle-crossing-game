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

# Initialize objects
sb = Scoreboard()
dog = Player()
car_manager = CarManager()

# Listen for keypress
screen.listen()
screen.onkey(dog.move, "Up")

# PLay game
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect if car hit turtle
    for car in car_manager.cars:
        if car.distance(dog) < 20:
            game_running = False
            sb.game_over()

    # Detect if turtle crossed successfully
    if dog.at_finish_line():
        car_manager.level_up()
        dog.level_up()
        sb.display_level(dog.level)
        dog.go_to_start()

screen.exitonclick()
