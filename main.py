"""
The main program for my CS 350 BDD project
"""
from graphviz import Source
from my_functions import *

# BDD vars
#TODO: I dont understand this, i added them to cover my bases
# x1, x2, x3, x4, x5 = bddvars('x', 5)
# y1, y2, y3, y4, y5 = bddvars('y', 5)
# x_1, x_2, x_3, x_4, x_5 = bddvars('x_', 5)
# y_1, y_2, y_3, y_4, y_5 = bddvars('y_', 5)
x_1 = exprvar('x_1')
x_2 = exprvar('x_2')
x_3 = exprvar('x_3')
x_4 = exprvar('x_4')
x_5 = exprvar('x_5')

y_1 = exprvar('y_1')
y_2 = exprvar('y_2')
y_3 = exprvar('y_3')
y_4 = exprvar('y_4')
y_5 = exprvar('y_5')
# a, b, c, d, e = map(exprvar, 'abcde')
# v, w, x, y, z = map(exprvar, 'vwxyz')

# even and prime arrays
even = [i for i in range(32) if i%2 is 0]
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# edge array
edges = [(i,j) for i in range(32) for j in range(32) if (i+3)%32 is j%32 or (i+8)%32 is j%32]

# get the BDD for the set of even numbers
even_boolean_formula = list_to_boolean_formula(even, 'y')
# print(even_boolean_formula)
even_BDD = expr2bdd(even_boolean_formula)

# get the BDD for the set of prime numbers
prime_boolean_formula = list_to_boolean_formula(prime, 'x')
print(prime_boolean_formula)
prime_BDD = expr2bdd(prime_boolean_formula)

# get the BDD for the set of edges
edge_boolean_formula = edge_list_to_boolean_formula(edges)
# print(edge_boolean_formula)
edge_BDD = expr2bdd(edge_boolean_formula)

# print(list(prime_BDD.satisfy_all()))

# gv = Source(prime_BDD.to_dot())
# gv.render("prime", view=True)

test = edge_boolean_formula.restrict({x_1: 1, x_2: 1, x_3: 0, x_4:1, x_5:1,y_1:0,y_2:0,y_3:0,y_4:1,y_5:1})
test = str(test)
print(test)
# gv = Source(test.to_dot())
# gv.render("test", view=True)