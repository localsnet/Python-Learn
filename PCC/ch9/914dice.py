#!/usr/bin/python3
from random import randint

class Die():
 """Dice model"""
 def __init__(self, sides=6):
  """Initialize attributes"""
  self.sides = sides
 
 def roll_die(self):
  """Method prints a random number between 1 and the number of sides the die has"""
  x = randint(1, self.sides) #None catching in list  cause:Python adds return None to the end of any function definition with no return statement 
  return x

#On my own automation
 def roll_ten(self):
  """Method roll die 10 times"""
  results = []
  #result = self.roll_die()
  for roll in range(10):
   results.append(self.roll_die())
  print (results)

print("------------------------------- 6-sided die default")
# 6-sided die default
inst1 = Die()
inst1.roll_ten()

print("------------------------------- 10-sided die")

# 10-sided die
inst2 = Die(10)
inst2.roll_ten()

print("------------------------------- 20-sided die")

# 20-sided die
inst3 = Die(20)
inst3.roll_ten()

