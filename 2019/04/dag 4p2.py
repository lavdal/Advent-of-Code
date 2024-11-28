# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:59:56 2020

@author: EBL
"""

puzzle_seed = range(146810,612564)

def stiger(num):
  
  num = list(str(num))
  if num == sorted(num):
    return True
  else:
    return False

def unikke_cifre(num): #eller er der to som går igen?
    num = str(num)
    return len(num) == len(set(num))
  
def har_dubletter(num):
  num = list(str(num))
  for i in range(len(num)-1):
    if num[i] == num[i+1] and \
      (i == 0 or num[i] != num[i-1]) and \
      (i == 4 or num[i] != num[i+2]):
        return True
  return False

def solve():
  mulige = 0
  for svar in puzzle_seed:
    if stiger(svar):
      if har_dubletter(svar):
        mulige +=1
  return mulige
        
print(solve())
  

