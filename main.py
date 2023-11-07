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



# 3.1 TESTS
# test: RR(27,3)
test = RR_expr.restrict({x1: 1, x2: 1, x3: 0, x4:1, x5:1,y1:0,y2:0,y3:0,y4:1,y5:1})
print("RR(27,3): " + str(test))

# test: RR(16,20)
test = RR_expr.restrict({x1: 1, x2: 0, x3: 0, x4: 0, x5: 0, y1: 1, y2: 0, y3: 1, y4: 1, y5: 1})
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
z1 = exprvar('z1')
z2 = exprvar('z2')
z3 = exprvar('z3')
z4 = exprvar('z4')
z5 = exprvar('z5')

# get the RR for even to intermediate node and RR for intermediate node to prime
RR_temp1 = RR_expr
RR_temp2 = RR_expr
RR_temp1 = RR_temp1.compose({y1:z1, y2:z2, y3:z3, y4:z4, y5:z5})
RR_temp2 = RR_temp2.compose({x1:z1, x2:z2, x3:z3, x4:z4, x5:z5})

# combine the expression
RR2_expr = RR_temp1 & RR_temp2

# remove the intermediate node's variables
RR2_expr = RR2_expr.smoothing({z1, z2, z3, z4, z5})

# BBD for RR2
RR2_BDD = expr2bdd(RR2_expr)

# 3.2 TESTS
# test: RR2(27,6)
test = RR2_expr.restrict({x1: 1, x2: 1, x3: 0, x4:1, x5:1,y1:0,y2:0,y3:1,y4:1,y5:0})
print("RR2(27,6): " + str(test))

# test: RR2(27,9)
test = RR2_expr.restrict({x1: 1, x2: 1, x3: 0, x4:1, x5:1, y1:0,y2:1,y3:0,y4:0,y5:1})
print("RR2(27,9): " + str(test))

# COMPUTE RR2* FOR RR2
x1, x2, x3, x4, x5 = bddvars('x', 5)
y1, y2, y3, y4, y5 = bddvars('y', 5)
z1, z2, z3, z4, z5 = bddvars('z', 5)
RR2 = expr2bdd(RR2_expr)
R = RR2
H = R
H_prime = None
while True:
    # print("h")
    H_prime = H
    # H_prime
    t1 = H.compose({y1:z1, y2:z2, y3:z3, y4:z4, y5:z5}) 

    # R
    t2 = R.compose({x1:z1, x2:z2, x3:z3, x4:z4, x5:z5})
    # print("finished composing")

    # H_prime | H_prime o R
    t = t1 & t2
    # trans_close = trans_close.smoothing((z1, z2, z3, z4, z5))
    H = H_prime | t
    # print("finished logic")
    H = H.smoothing((z1, z2, z3, z4, z5))

    if H.equivalent(H_prime):
        # H is R* 
        break
# GENERATE A PDF OF A BDD
# h_test = H.smoothing(y1).smoothing(y2).smoothing(y3).smoothing(y4).smoothing(y5)
# gv = Source(h_test.to_dot())
# gv.render("h_test", view=True)


x1 = exprvar('x1')
x2 = exprvar('x2')
x3 = exprvar('x3')
x4 = exprvar('x4')
x5 = exprvar('x5')

y1 = exprvar('y1')
y2 = exprvar('y2')
y3 = exprvar('y3')
y4 = exprvar('y4')
y5 = exprvar('y5')

RR2star = bdd2expr(H)
PRIME = prime_boolean_formula
EVEN = even_boolean_formula
# RR2star = H 
# PRIME = prime_BDD
# EVEN = even_BDD

banana = EVEN & RR2star
apple = banana.smoothing(y1).smoothing(y2).smoothing(y3).smoothing(y4).smoothing(y5)

fish = ((~PRIME) | apple)
ans = ~((~fish).smoothing(x1).smoothing(x2).smoothing(x3).smoothing(x4).smoothing(x5))
# ans = expr2bdd(ans)

if ans.equivalent(True):
    print(f"Statement A is {ans.equivalent(True)}")
else:
    print(f"Statement A is {ans.equivalent(True)}")

