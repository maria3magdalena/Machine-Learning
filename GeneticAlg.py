# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:28:56 2023

@author: Dom
"""


import random
import numpy as np

class Puzzle:
 
 def __init__(self, filepath):
             
  file = open(filepath, "r")
  #lines = file.split('\n')
 
  with open(filepath) as file:
    lines = []
    with open(filepath) as file:
      lines = [line.rstrip() for line in file]


  self.n = int(lines[0])
  i=1
  while(len(lines[i]) < self.n):
        i=i+1
       
  self.A = [[int(x) for x in lines[i+j].split()] for j in range(self.n)]
  
  i=i + self.n
 
  while(len(lines[i])<self.n):
        i=i+1
        
  self.D = [[int(x) for x in lines[i+j].split()] for j in range(self.n)]
  

      
class GeneticSolution:
    
#Pojedyncze osobniki sa reprezentowane przez macierze wymiaru nxn, takie, ze 1 wystepuje na wspolrzednej (i,j) 
#wtedy i tylko wtedy gdy na i-tym placu budowy stawiamy j-ty budynek
    
  def __init__(self, n_popul, puzzle):   #Tworzenie populacji poczatkowej
      
      self.n = puzzle.n
      self.A = puzzle.A
      self.D = puzzle.D
      self.population = []
      for p in range(n_popul):
         x = list(range(self.n))
         random.shuffle(x) 
         genom = x
         self.population.append(genom)
      self.numberpopul = n_popul
        
        

  def CalculateTotalErrors(self):
      Errors = []
            
      for genom in self.population:
      
          result = 0
     
          for i in range(self.n):
              for j in range(self.n):
                              
                  result = result + self.A[int(genom[i])][int(genom[j])]*self.D[i][j]
              
          Errors.append(result)
      return Errors
            
          
           
  def Selection (self, tournament_size):       #dokonuje ewaluacji osobnikow i selekcji
      
      fun_values = self.CalculateTotalErrors()     
     
      best_value =  min(fun_values)
              
      best_genom_ind = fun_values.index(best_value)
      best_genom = self.population[best_genom_ind]
      #wprowadzamy element strategii elitarnej: zachowujemy najlepszego osobnika w populacji biezacej
    
      newpopulation = []
               
      for i in range(self.numberpopul):  #dokonujemy selekcji metoda turniejowa
          S = []
          for j in range(tournament_size):
              ind = int(random.random()*self.numberpopul)
              S.append(ind)
          ranking = [fun_values[ind] for ind in S]
          winner_ind = S[ranking.index(min(ranking))]
          newpopulation.append( self.population[winner_ind])
         
         
      self.population = newpopulation
             
      return best_genom
  
  def Crossover(self):
    
    new_generation = []
    for i in range(int(self.numberpopul/2)):
       parents = []
       rand_ind1 = int(random.random()*len(self.population))
       parent1 = self.population[rand_ind1]
       del self.population[rand_ind1]
       parents.append(parent1)
       rand_ind2 = int(random.random()*len(self.population))
       parent2 = self.population[rand_ind2]
       del self.population[rand_ind2]
       parents.append(parent2)
       pointa = int(random.random()*(self.n -2))
       pointb = int(random.random()*(self.n -2))
       while pointb==pointa:
           pointb= int(random.random()*(self.n -2))
       point1 = min(pointa, pointb)
       point2 = max(pointa, pointb)
       
       offspring_a = np.zeros(self.n)
       offspring_a[point1:point2] = parents[1][point1:point2]
       already_used_genes = set(parents[1][point1:point2])

       i = 0
       p = 0

       while i<point1 and p<self.n:
           if parents[0][p] not in already_used_genes:
               offspring_a[i] = parents[0][p]
               already_used_genes.add(parents[0][p])
               i+=1
          
           p+=1
           
       j = point2 + 1

       while j<self.n and p<self.n:
           if parents[0][p] not in already_used_genes:
               offspring_a[j] = parents[0][p]
               already_used_genes.add(parents[0][p])
               j+=1
           
           p+=1
      
       new_generation.append(offspring_a)
       
           
       offspring_b = np.zeros(self.n)
       offspring_b[point1:point2] = parents[0][point1:point2]
       already_used_genes = set(parents[0][point1:point2])

       i = 0
       p = 0

       while i<point1 and p<self.n:
           if parents[1][p] not in already_used_genes:
               offspring_b[i] = parents[1][p]
               already_used_genes.add(parents[1][p])
               i+=1
          
           p+=1
           
       j = point2 + 1

       while j<self.n and p<self.n:
           if parents[1][p] not in already_used_genes:
               offspring_b[j] = parents[1][p]
               already_used_genes.add(parents[1][p])
               j+=1
           
           p+=1
       
       new_generation.append(offspring_b)
       
       self.population = new_generation
       self.numberpopul = len(new_generation)
                   
                   
    
  def Mutation( self, probability = 0.5):  
    
    for i in range( self.numberpopul -1):
       if random.random() < probability:
              inds = random.choices(range(self.n), k=2)
              mut = self.population[i]
              pom = mut[inds[0]]
              mut[inds[0]] = mut[inds[1]]
              mut[inds[1]] = pom
              self.population[i] = mut
             
 