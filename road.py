from turtle import Turtle

class Road(Turtle):
   def __init__(self):
      super().__init__()
      self.hideturtle()
      self.penup()
      self.color('red')

      for y in range(-240,241,60):
         self.goto(-300,y)
         self.draw_line()

   def draw_line(self):
      for _ in range(20):
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(10)
