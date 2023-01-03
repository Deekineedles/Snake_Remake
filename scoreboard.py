from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def got_food(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
