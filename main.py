import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


Jimmy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Jimmy.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detecting collision with the car
    for car in car_manager.all_cars:
        if Jimmy.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detecting if Jimmu reached the other side
    if Jimmy.ycor() == 280:
        Jimmy.reset()
        car_manager.next_level()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
screen.exitonclick()
