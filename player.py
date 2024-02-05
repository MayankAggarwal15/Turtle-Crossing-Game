from turtle import Turtle

move_distance = 10

turtle_width = 1
turtle_length = 1
turtle_outline = 1

class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.shapesize(turtle_width,turtle_length,turtle_outline)
        self.speed(0)
        self.seth(90)
        self.penup()
        self.reset_position()

    def move_up(self):
        self.forward(move_distance)

    def reset_position(self):
        self.goto(200,-280)
