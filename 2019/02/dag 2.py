# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:40:38 2020

@author: EBL
"""

input_code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

def perform_calc(noun, verb, input_liste, facit):
  liste=input_liste.copy()
  liste[1]= noun
  liste[2]= verb
  
  for num in range(0,len(liste),4):
    if liste[num] == 1:
      res_location = liste[num+3]
      var_a = liste[num+1]
      var_b = liste[num+2]
      res = liste[var_a] + liste[var_b]
      #print(f"skriver {res} til lokationen {res_location}")
      liste[res_location]=res
      #print(liste)
      
    elif liste[num] == 2:
      res_location = liste[num+3]
      var_a = liste[num+1]
      var_b = liste[num+2]
      res = liste[var_a] * liste[var_b]
      #print(f"skriver {res} til lokationen {res_location}")
      liste[res_location]=res
      #print(liste)
    elif liste[num] == 99:
      #print(saet)
      #print(f"afsluttet korrekt position 0 er: {liste[0]}\n{liste}\nverb: {verb}\nnoun: {noun}\n---")
      if liste[0] == facit:
        print(f"succes! noun: er {noun}; og verb er {verb}; svaret er {100*noun+verb}")
        #return(noun*verb*100)
        return liste[0]
#      else:
#        return(None)
    else:
      #print(f"noget gik galt. Mødte nummer {[num]}")
      #print(f"noun: {noun} - verb: {verb} - [0] : {liste[0]}")
      break

for verb in range(0,100):
  for noun in range(0,100):
    #print(f"noun={noun}; verb={verb}")
    perform_calc(int(noun),int(verb),input_code,19690720)

#for verb in range(12):
#  for noun in range(12):
#    output = perform_calc(noun, verb, input_code.copy(), 3085697)
#    if output != None:
#      print(output)