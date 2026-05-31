import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=Player()
car_manager = CarManager()
scoreboard = Scoreboard()
# road=Road()
screen.listen()
screen.onkey(player.go_up,'Up')
screen.onkey(player.go_back,'Down')


game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()

  car_manager.create_car()
  car_manager.move_car()

  """detecting the collosion of cars"""
  for car in car_manager.all_cars:
    if car.distance(player) < 20:
      scoreboard.lose_life()
      player.go_to_start()

      if scoreboard.lives == 0:
        game_is_on = False
        scoreboard.check_high_score()
        scoreboard.game_over()
  
  """detecting successfull crossing"""
  if player.is_at_finish():
    player.go_to_start()
    car_manager.level_up()
    scoreboard.increase_level()



screen.exitonclick()