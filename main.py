#1 Functional Prompt:

def x(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# How does this solution ensure data immutability?
'''
The function breaks the array and append in to two parts.
'''
#Is this solution a pure function? Why or why not?
'''
The Array is empty allowing the data provided the only variable.
'''
#Is this solution a higher order function? Why or why not?
'''
yes the Arr is part of the function with the two (for i in x).
'''
#Would it have been easier to solve this problem using a different programming style?
'''
Python is more simplified compared to JavaScript
'''
#Why in particular is functional programming a helpful paradigm when solving this problem?
'''
It allows us to break down the parts to make it easier to work on.
'''

# 2 Object Oriented Prompt

def podRacers(self, max_speed, condition, price):
  self.max_speed = max_speed
  self.condition = condition
  self.price = price

def repair(self):
  self.condition = "repaired"

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"
  
'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
'''
#Encapsulation: The first part where the function is wraped together.
#Abstraction: Being able to name the parts of the function to seperate them from other parts.
#Inheritance: the call back to the first function's parts.
#Polymorphism: This might be how the parts could be used in any way it needs.
'''
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
'''
# No if in JavaScript there would be over 5 functions.
'''
How in particular did Object Oriented Programming assist in the solving of this problem?
'''
# The break down of the parts and taskes needed to do.