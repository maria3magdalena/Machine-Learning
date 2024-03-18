# -*- coding: utf-8 -*-

import GeneticAlg

def Solve(filepath, n_popul, tournament_size, n_iter, mutation_probability = 0.5):
    puzzle = Puzzle(filepath)
    genetic = GeneticSolution(n_popul, puzzle)
    
    for i in range(n_iter):
        
       best_genom = genetic.Selection(tournament_size)
       genetic.Crossover()
       genetic.Mutation(mutation_probability)
       genetic.population.append(best_genom)
       genetic.numberpopul +=1
       
    func_values = genetic.CalculateTotalErrors()     
    best_value =  min(func_values)
    best_genom_ind = func_values.index(best_value)
    best_genom = genetic.population[best_genom_ind]
              
    return best_genom, best_value
 