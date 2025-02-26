from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.ht()
        self.color("white")
        self.teleport(0, 280)
        self.printing_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.printing_score()

    def clear_score(self):
        self.clear()
        self.printing_score()

    def printing_score(self):
        self.write(f"Your Score = {self.score} Highest Score: {self.highest_score}", align="center",
                   font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(f"{self.score}")
            with open("highest_score.txt") as file:
                file.read()
        self.score = 0
        self.clear_score()
