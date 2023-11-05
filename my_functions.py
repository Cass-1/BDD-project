"""
The helper functions I wrote for my CS 350 BDD project
"""
from typing import List, Tuple
from pyeda.inter import *

def number_to_boolean_formula(num: int, var: str) -> str:
    """
    Given a base ten number return the boolean formula 
    (represented in string form) for that number
    """
    #NOTE: the reason that the number is in string for is it makes it easier
    #      to add multiple boolean formulas together, which is needed later
    
    # covert the base 10 number to five digit binary
    binary_num = f"{num:05b}"
    # print(binary_num)

    # loop through binary to create the boolean formula
    boolean_formula = ""
    position = 1
    for digit in binary_num:
        if int(digit) is 0:
            boolean_formula += f" ~{var}{position} &"
        elif int(digit) is 1:
            boolean_formula += f" {var}{position} &"
        else:
            print("Something has gone wrong")

        position += 1

    # remove the last (hanging) ampersand and return
    boolean_formula = boolean_formula[:-1]
    return boolean_formula

def list_to_boolean_formula(list: List[int], var: str):
    """
    Given a list of integers, return the boolean formula
    (in expression form) for that list.
    """
    boolean_formula = ""
    for num in list:
        boolean_formula += number_to_boolean_formula(num, var) + "|"
    
    # remove last (hanging) "|"
    boolean_formula = boolean_formula[:-1]
    return expr(boolean_formula)

def edge_to_boolean_formula(tup: Tuple[int,int]) -> str:
    """
    Takes a tuple of two integers which represents the edge 
    from node Tuple[0] to Tuple[1] and returns the boolean
    formula (in string form) of that edge
    """
    # get the 5 digit binary representation of both elements
    # in the tuple
    first_binary_num = f"{tup[0]:05b}"
    second_binary_num = f"{tup[1]:05b}"

    # create the boolean formula string for the first number
    position = 1
    first_boolean_formula = ""
    for bit in first_binary_num:
        if int(bit) is 0:
            first_boolean_formula += f" ~x{position} &"
        elif int(bit) is 1:
            first_boolean_formula += f" x{position} &"
        else:
            print("Something has gone wrong")
        position += 1
    first_boolean_formula = first_boolean_formula[:-1]

    # create the boolean formula string for the second number
    position = 1
    second_boolean_formula = ""
    for bit in second_binary_num:
        if int(bit) is 0:
            second_boolean_formula += f" ~y{position} &"
        elif int(bit) is 1:
            second_boolean_formula += f" y{position} &"
        else:
            print("Something has gone wrong")
        position += 1
    second_boolean_formula = second_boolean_formula[:-1]

    # put the two boolean formulas together
    boolean_formula = first_boolean_formula + " & " + second_boolean_formula

    return boolean_formula

def edge_list_to_boolean_formula(list: List[Tuple[int,int]]):
    """
    Given a list of edges, return the boolean formula
    (in expression form) for that list.
    """
    boolean_formula = ""
    for tup in list:
        boolean_formula += edge_to_boolean_formula(tup) + "|"
    
    # remove last (hanging) "|"
    boolean_formula = boolean_formula[:-1]
    return expr(boolean_formula)
