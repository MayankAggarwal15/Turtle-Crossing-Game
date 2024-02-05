from turtle import Turtle
import random

move_distance = 10

car_width = 1
car_length = 3
car_outline = 1


class Car:

    def __init__(self):

        self.cars_list = []
        
        self.rvalue = 0
        self.gvalue = 0
        self.bvalue = 0

        self.move_speed = move_distance

    def create_car(self):
        chance = random.randint(1,5)

        if chance == 5:
            car = Turtle(shape="square")
            car.shapesize(car_width,car_length,car_outline)
            car.color(self.rvalue , self.gvalue , self.bvalue)
            car.penup()
            car.speed(0)
            car_y = random.randint(-240 , 240)
            car.goto(470, car_y)

            self.cars_list.append(car)


    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.move_speed)

    def remove_cars(self):
        for car in self.cars_list:
            if car.xcor() < -60:
                car.hideturtle()

    def car_color(self):
        r = random.randint(0, 200)
        g = random.randint(0, 200)
        b = random.randint(0, 200)

        self.rvalue = r
        self.gvalue = g
        self.bvalue = b


        
