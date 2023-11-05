"""
The main program for my CS 350 BDD project
"""
from my_functions import *

# even and prime arrays
even = [i for i in range(32) if i%2 is 0]
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# edge array
edges = [(i,j) for i in range(32) for j in range(32) if (i+3)%32 is j%32 or (i+8)%32 is j%32]

# get the BDD for the set of even numbers
even_boolean_formula = list_to_boolean_formula(even, 'y')
print(even_boolean_formula)
even_BDD = expr2bdd(even_boolean_formula)

# get the BDD for the set of prime numbers
prime_boolean_formula = list_to_boolean_formula(prime, 'x')
prime_BDD = expr2bdd(prime_boolean_formula)

# get the BDD for the set of edges
edge_boolean_formula = edge_list_to_boolean_formula(edges)
edge_BDD = expr2bdd(edge_boolean_formula)
