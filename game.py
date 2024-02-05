# PROJECT ON TURTLE CROSSING GAME

from turtle import Screen , Turtle
import time
from player import Player
from boundary import Boundary
from score import Score
from cars import Car


myscreen = Screen()
myscreen.setup(1350,1000,0,0)
myscreen.title("TURTLE CROSSING GAME")
myscreen.colormode(255)
myscreen.bgcolor("grey")

myscreen.tracer(0)

boundary = Boundary()
player = Player()
car = Car()
score = Score()
logo = Score()

logo.game_logo()
logo.game_attributes()
score.scoreboard()

myscreen.update()

myscreen.listen()

myscreen.onkeypress(player.move_up, "Up")

end = False

timer = 0.1

while not end:
    myscreen.update()
    time.sleep(timer)

    car.car_color()
    car.create_car()
    car.move_cars()
    car.remove_cars()

    if player.ycor() >= 270:
        score.scoreboard()
        player.reset_position()
        timer *= 0.5

    for cars in car.cars_list:
        if player.distance(cars) < 20:
            end = True
            score.game_over()


    


myscreen.exitonclick()


