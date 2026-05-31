from turtle import Turtle
import random

COLORS = ['red','orange','yellow','blue','green','purple']
LANES = [-240,-180,-120,-60,0,60,120,180,240]
STARTING_MOVE_DISTANCE =5
MOVE_INCREMENT =3


class CarManager:
  def __init__(self):
    self.all_cars=[]
    self.car_speed =STARTING_MOVE_DISTANCE
  
  def create_car(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      new_car=Turtle('square')
      new_car.shapesize(stretch_wid=1,stretch_len=3)
      new_car.penup()
      new_car.color(random.choice(COLORS))
      random_y = random.choice(LANES)
      new_car.goto(300,random_y)
      self.all_cars.append(new_car)

  def move_car(self):
    for car in self.all_cars[:]:
      car.backward(self.car_speed)

      if car.xcor() <-320:
        car.hideturtle()
        self.all_cars.remove(car)

  def level_up(self):
    self.car_speed += MOVE_INCREMENT
