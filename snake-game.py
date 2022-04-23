import time
from turtle import Screen
# from snake import Snake
from snake2 import Snake
from snakefood import Food
from snakescoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("*** CENTIPEDE GAME ***")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

keep_moving = True

while keep_moving:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.new_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # keep_moving = False
        # score.game_over()
        score.check_score()
        snake.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # keep_moving = False
            # score.game_over()
            score.check_score()
            snake.game_over()

screen.exitonclick()