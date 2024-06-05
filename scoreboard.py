from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
