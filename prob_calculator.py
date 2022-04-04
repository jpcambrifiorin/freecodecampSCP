import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:

  def __init__(self,**kwargs):
    self.contents=[]
    for a in kwargs:
      for b in range(kwargs[a]):
        self.contents.append(a)

  def draw(self,number):
    randomBalls=[]

    if number>len(self.contents):
      return self.contents
    
    for i in range(number):
      rnum = random.randrange(len(self.contents))
      randomBalls.append(self.contents[rnum])
      self.contents.pop(rnum)

    return randomBalls



def experiment(hat,expected_balls:dict,num_balls_drawn:int,num_experiments:int):
  flag=True
  M=0
  hat_copy=copy.deepcopy(hat)

  for i in range(num_experiments):
    draw_balls = hat.draw(num_balls_drawn)
    
    for j in expected_balls.keys():
      if draw_balls.count(j)<expected_balls[j]:
        flag=False
    
    if flag:
      M = M+1

    flag=True
    hat=copy.deepcopy(hat_copy)

  return round(M/num_experiments,3)
  