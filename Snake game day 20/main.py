from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
user_lvl = screen.textinput("Choose lvl", "Choose difficulty level: \"easy\", \"medium\", \"hard\"").lower()
user_wall = screen.textinput("Choose wall physics", "Do you want to have a wall on screen edge? "
                                                    "Type \"y\" or \"n\"").lower()
screen.tracer(0)
screen.listen()
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")


def snake_ate_food():
    """Detect collision with food, add one pixel to snake body and adding scores"""
    if snake.head.distance(food) < 5:
        snake.add_pixel_after_eating()
        food.refresh()
        scoreboard.update_score()

        # Create food in coordinates different from snake body
    for position in range(len(snake.full_body_list)):
        if food.distance(snake.full_body_list[position]) < 1:
            food.refresh()


game_is_on = True

while game_is_on:
    if user_lvl == "easy":
        time.sleep(0.3)
    elif user_lvl == "medium":
        time.sleep(0.15)
    elif user_lvl == "hard":
        time.sleep(0.07)

    screen.update()
    snake.snake_move()
    snake_ate_food()

    # Detect collision with wall
    if user_wall == "y":
        if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over_hit_wall()
            scoreboard.reset()
    elif user_wall == "n":
        if snake.head.xcor() < -290:
            snake.head.setx(300)
        elif snake.head.xcor() > 290:
            snake.head.setx(-300)
        elif snake.head.ycor() > 290:
            snake.head.sety(-300)
        elif snake.head.ycor() < -290:
            snake.head.sety(300)

    # Detect collision with its tail
    for position in range(1, len(snake.full_body_list)):
        if snake.head.distance(snake.full_body_list[position]) < 1:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over_hit_snake()

screen.exitonclick()
