from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

   #Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.got_food()
#     Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.head.setposition(-280, snake.head.ycor())
        # scoreboard.reset()
        # snake.reset()


#         Detect collision with tail
    for pieces in snake.body_pieces[1:]:
        if snake.head.distance(pieces) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
