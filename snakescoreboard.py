from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 12, "bold")

with open("high_score.txt", 'r') as saved_high_score:
    for numb in saved_high_score:
        previous_high_score = int(numb)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.high_score = previous_high_score
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("red")
        self.score()

    def score(self):
        self.clear()
        self.write(f"Score: {self.counter}  High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER! ", align=ALIGNMENT, font=FONT)

    def check_score(self):
        if self.counter > self.high_score:
            self.high_score = self.counter
            with open("high_score.txt", 'w') as new_saved_score:
                new_saved_score.write(str(self.high_score))
        self.counter = 0
        self.score()

    def new_score(self):
        self.counter += 1
        self.score()
