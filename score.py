from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.game_level = 0
        self.color("black")
        self.hideturtle()
        self.speed(0)
        self.penup()
        
    def scoreboard(self):
        self.clear()
        self.goto(200,310)
        self.game_level += 1
        self.string1 = f"LEVEL : {self.game_level}"
        self.write(self.string1 , False , "center" , ("Calibri" , 30 , "bold"))
    

    def game_over(self):
        self.goto(200,0)
        self.write("GAME OVER" , False , "center" , ("Cambria" , 30 , "bold"))

    def game_logo(self):
        self.goto(-400,80)
        self.write("TURTLE" , False , "center" , ("Algerian" , 80 , "bold"))
        self.goto(-400,-80)
        self.write("CROSSING" , False , "center" , ("Algerian" , 80 , "bold"))

    def game_attributes(self):
        self.goto(575,-290)
        self.write("START" , False , "center" , ("Cambria" , 20 , "bold"))
        self.goto(575,270)
        self.write("FINISH" , False , "center" , ("Cambria" , 20 , "bold"))

