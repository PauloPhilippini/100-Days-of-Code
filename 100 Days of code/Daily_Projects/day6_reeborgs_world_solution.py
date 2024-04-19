'''Solution for Reeborg Hurdle 1'''

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

for step in range(6):
  jump()

#Hurdle 2
'''Solution for Reeborg Hurdle 2'''
#while not at_goal():
#  jump()
#    
#
#

#Hurdle 3
'''Solution for Reeborg Hurdle 3'''
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()


#Hurdle 4 
'''Solution for Reeborg Hurdle 4'''
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  while wall_on_right():
      move()
  turn_right()
  move()
  turn_right()
  while front_is_clear():
      move()
  turn_left()

while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()

#Maze
'''Solution for Reeborg Maze'''
def turn_right():
  turn_left()
  turn_left()
  turn_left()

while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
    move()
  else:
    turn_left()

#Challanges 1 2 3 solution
def turn_right():
  turn_left()
  turn_left()
  turn_left()

while not at_goal():
  if right_is_clear() and front_is_clear() == False:
    turn_right()
    move()
  elif front_is_clear():
    move()
  elif right_is_clear():
    turn_left()
    move()
  else:
    turn_left()