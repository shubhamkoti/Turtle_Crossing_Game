from turtle import Turtle

FONT =("Courier",20,"normal")

class Scoreboard(Turtle):
  def __init__(self):
      super().__init__()
      self.level=1
      self.lives=3
      with open('score.txt') as file:
         self.high_score = int(file.read())

      self.hideturtle()
      self.penup()
      self.goto(-280,210)
      self.update_scoreboard()
      
  
  def update_scoreboard(self):
     self.clear()
     self.write(f'Level :{self.level}\nLives :{self.lives}\nHigh Score: {self.high_score}',align='left',font=FONT)


  def increase_level(self):
    
    self.level +=1
    self.update_scoreboard()
    
  def game_over(self):
     self.goto(0,0)
     self.write(f'Game Over\nHigh Score: {self.high_score}', align='center',font=FONT)

  def lose_life(self):
     self.lives -=1
     self.update_scoreboard()

  def check_high_score(self):
     if self.high_score < self.level :
        self.high_score = self.level

        with open('score.txt','w')as f:
           f.write(str(self.high_score))
