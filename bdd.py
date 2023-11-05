from pyeda.inter import *

def number_to_boolean_formula(num):
    """
    Given a base ten number return the boolean formula for that number
    """
    
    binary = f'{num:05b}'

    return binary

# even and prime arrays
even = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

print(number_to_boolean_formula(3));
