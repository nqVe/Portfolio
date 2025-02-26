from turtle import Turtle
MOVE_INSTANCE = 20


class Snake:
    def __init__(self):
        # self.x_pos = 0
        # self.full_body_list_position = []
        self.full_body_list = []
        self.snake_body()
        self.head = self.full_body_list[0]

    def snake_body(self):
        """Create snake body. Takes variable to create number of pixels that snake body contains"""
        for snake_pix in range(5):
            self.x_pos = 0
            pixel = Turtle("square")
            pixel.color("white")
            pixel.penup()
            pixel.teleport(self.x_pos, 0)
            self.x_pos -= MOVE_INSTANCE
            self.full_body_list.append(pixel)

    def add_pixel_after_eating(self):
        """Adding pixel to snake body after eating food"""
        pixel = Turtle("square")
        pixel.color("white")
        pixel.penup()
        pixel.teleport(self.full_body_list[1].xcor(), self.full_body_list[1].ycor())
        self.full_body_list.append(pixel)

    def snake_move(self):
        """Function that makes snake move"""
        for parts in range(len(self.full_body_list) - 1, 0, -1):
            part_1 = self.full_body_list[parts]
            x_part_2 = self.full_body_list[parts - 1].xcor()
            y_part_2 = self.full_body_list[parts - 1].ycor()
            part_1.teleport(x_part_2, y_part_2)
        self.head.forward(MOVE_INSTANCE)

    def turn_left(self):
        """Turn left snake body"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        for seg in self.full_body_list:
            seg.goto(1000, 1000)
        self.full_body_list.clear()
        self.snake_body()
        self.head = self.full_body_list[0]
        # self.full_body_list.home()

    def turn_right(self):
        """Turn right snake body"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_up(self):
        """Set snake head to north"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        """Set snake head to south"""
        if self.head.heading() != 90:
            self.head.setheading(270)
