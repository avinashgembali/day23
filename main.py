from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score
import time

s = Screen()
s.title("turtle cross")
s.setup(width=600, height=600)
s.tracer(0)


t = Player()
s.listen()
s.onkey(t.move, "Up")
c = CarManager()
score = Score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    c.create_car()
    c.move_cars()

    # if car collide with turtle
    for car in c.all_cars:
        if t.distance(car) < 30:
            game_is_on = False
            score.game_over()

    if t.is_at_finish_line():
        t.go_to_start()
        c.level_up()
        score.level_inc()

s.exitonclick()
