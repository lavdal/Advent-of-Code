# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:36:04 2020

@author: EBL
"""
#ruter = ["R8,U5,L5,D3","U7,R6,D4,L4"]

from collections import defaultdict

def manhattah(pos):
  return abs(pos[0]) + abs(pos[1])

def get_wire_positions(wire):
  x = 0
  y = 0
  positions =set()
  for i in range(len(wire)):
    for _ in range(int(wire[i][1:])):
      direction = wire[i][0]
      #print(direction)
      if   direction == "R":
          x +=1
      elif direction == "L":
          x -=1
      elif direction == "D":
          y +=1
      elif direction == "U":
          y -=1
      positions.add((x, y))
  return positions

def get_steps_to_crossing (wire, crossings):
  crossing = defaultdict(int)
  distance = 0
  x, y = 0, 0
  
  for i in range(len(wire)):
    for _ in range(int(wire[i][1:])):
      direction = wire[i][0]
      if direction == "R":
          x +=1
      elif direction == "L":
          x -=1
      elif direction == "D":
          y +=1
      elif direction == "U":
          y -=1
      
      distance +=1
      
      if (x,y) in crossings:
        crossing[(x, y)] = distance
  return crossing

#get_wire_positions(rute_a)
fil = open(r"03input.txt", "r")
ruter = fil.readlines()
rute_a = ruter[0].split(",")
rute_b = ruter[1].split(",")

a_pos = get_wire_positions(rute_a)
b_pos = get_wire_positions(rute_b)

mulige_kryds = set()

for a in a_pos:
  if a in b_pos:
    mulige_kryds.add(a)
    
a_steps = get_steps_to_crossing(rute_a, mulige_kryds)
b_steps = get_steps_to_crossing(rute_b, mulige_kryds)

least_steps = min(a_steps[kryds] + b_steps[kryds] for kryds in mulige_kryds)
print(least_steps)


#print(min(manhattah(i)for i in mulige_kryds))
