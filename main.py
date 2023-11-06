"""
The main program for my CS 350 BDD project
"""
from graphviz import Source
from my_functions import *

# BDD VARS
# Even
y1 = exprvar('y1')
y2 = exprvar('y2')
y3 = exprvar('y3')
y4 = exprvar('y4')
y5 = exprvar('y5')

# Prime
x1 = exprvar('x1')
x2 = exprvar('x2')
x3 = exprvar('x3')
x4 = exprvar('x4')
x5 = exprvar('x5')

# R
#NOTE: the reason for not reusing x1 ... x5 and y1 ... y5 is that for some reason the pyeda
# function expr() (which turns a string to an expression) flips the variable order to y's
# then x's if I reused x1...x5 and y1...y5
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

# x_1, x_2, x_3, x_4, x_5 = bddvars('x',5)
# y_1, y_2, y_3, y_4, y_5 = bddvars('y',5)

# DEFINING SETS
# even and prime sets
even = [i for i in range(32) if i%2 is 0]
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# edge set
edges = [(i,j) for i in range(32) for j in range(32) if (i+3)%32 is j%32 or (i+8)%32 is j%32]

# GET THE BDD FOR THE SETS
# even
even_boolean_formula = list_to_boolean_formula(even, 'y')
even_BDD = expr2bdd(even_boolean_formula)

# prime
prime_boolean_formula = list_to_boolean_formula(prime, 'x')
prime_BDD = expr2bdd(prime_boolean_formula)

# edges
RR_expr = edge_list_to_boolean_formula(edges)
RR_BDD = expr2bdd(RR_expr)

# GENERATE A PDF OF A BDD
# gv = Source(prime_BDD.to_dot())
# gv.render("prime", view=True)

# 3.1 TESTS
# test: RR(27,3)
test = RR_expr.restrict({x_1: 1, x_2: 1, x_3: 0, x_4:1, x_5:1,y_1:0,y_2:0,y_3:0,y_4:1,y_5:1})
print("RR(27,3): " + str(test))

# test: RR(16,20)
test = RR_expr.restrict({x_1: 1, x_2: 0, x_3: 0, x_4: 0, x_5: 0, y_1: 1, y_2: 0, y_3: 1, y_4: 1, y_5: 1})
print("RR(16,20): " + str(test))

# test: EVEN(14)
test = even_boolean_formula.restrict({y1: 0, y2: 1, y3: 1, y4: 1, y5: 0})
print("EVEN(14): " + str(test))

# test: EVEN(13)
test = even_boolean_formula.restrict({y1: 0, y2: 1, y3: 1, y4: 0, y5: 1})
print("EVEN(13): " + str(test))

# test: PRIME(7)
test = prime_boolean_formula.restrict({x1: 0, x2: 0, x3: 1, x4: 1, x5: 1})
print("PRIME(7): " + str(test))

# test: PRIME(2)
test = prime_boolean_formula.restrict({x1: 0, x2: 0, x3: 0, x4: 1, x5: 0})
print("PRIME(2): " + str(test))

# COMPUTE RR2
# define intermediate variables
z_1 = exprvar('z_1')
z_2 = exprvar('z_2')
z_3 = exprvar('z_3')
z_4 = exprvar('z_4')
z_5 = exprvar('z_5')

# get the RR for even to intermediate node and RR for intermediate node to prime
RR_even = RR_expr
RR_prime = RR_expr
RR_even = RR_even.compose({y_1:z_1, y_2:z_2, y_3:z_3, y_4:z_4, y_5:z_5})
RR_prime = RR_prime.compose({x_1:z_1, x_2:z_2, x_3:z_3, x_4:z_4, x_5:z_5})

# combine the expression
RR2_expr = RR_even & RR_prime

# remove the intermediate node's variables
RR2_expr = RR2_expr.smoothing({z_1, z_2, z_3, z_4, z_5})

# BBD for RR2
RR2_BDD = expr2bdd(RR2_expr)

# 3.2 TESTS
# test: RR2(27,6)
test = RR2_expr.restrict({x_1: 1, x_2: 1, x_3: 0, x_4:1, x_5:1,y_1:0,y_2:0,y_3:1,y_4:1,y_5:0})
print("RR2(27,6): " + str(test))

# test: RR2(27,9)
test = RR2_expr.restrict({x_1: 1, x_2: 1, x_3: 0, x_4:1, x_5:1, y_1:0,y_2:1,y_3:0,y_4:0,y_5:1})
print("RR2(27,9): " + str(test))

# COMPUTE RR2* FOR RR2
R = RR2_expr
H = R
H_prime = None
while True:
    # print("h")
    H_prime = H
    # H_prime
    t1 = H.compose({y_1:z_1, y_2:z_2, y_3:z_3, y_4:z_4, y_5:z_5}) 

    # R
    t2 = R.compose({x_1:z_1, x_2:z_2, x_3:z_3, x_4:z_4, x_5:z_5})
    # print("finished composing")

    # H_prime | H_prime o R
    t = t1 & t2
    # trans_close = trans_close.smoothing((z_1, z_2, z_3, z_4, z_5))
    H = H_prime | t
    # print("finished logic")
    H = H.smoothing((z_1, z_2, z_3, z_4, z_5))

    if H.equivalent(H_prime):
        # H is R* 
        break

RR2star_expr = H
RR2star_BDD = expr2bdd(H)
