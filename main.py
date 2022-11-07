from turtle import Turtle, Screen
from time import sleep
from utils.snake import Snake
from utils.food import Food
from utils.scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    
    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()
    
    #Detect collision with tail.
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            





screen.exitonclick()