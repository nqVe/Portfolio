from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("blue")
        self.shapesize(0.75)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Create food in random position"""
        random_x = random.choice(range(-280, 280, 20))
        random_y = random.choice(range(-280, 280, 20))
        self.teleport(random_x, random_y)


