from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level = {self.level}", move=False, align="left", font=FONT)

    def level_inc(self):
        self.level += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=FONT)
