"""
The main program for my CS 350 BDD project
"""
from functions import *

# even and prime arrays
even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# get the BDD for the set of even numbers
even_boolean_formula = list_to_boolean_formula(even)
even_BDD = expr2bdd(even_boolean_formula)

# get the BDD for the set of prime numbers
prime_boolean_formula = list_to_boolean_formula(prime)
prime_BDD = expr2bdd(prime_boolean_formula)