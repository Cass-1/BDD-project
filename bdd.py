from pyeda.inter import *

def number_to_boolean_formula(num):
    """
    Given a base ten number return the boolean formula for that number
    """
    # covert the base 10 to five digit binary
    binary_num = f"{num:05b}"
    print(binary_num)

    # loop through binary to create the boolean formula
    boolean_formula = ""
    position = 0
    for digit in binary_num:
        if int(digit) is 0:
            boolean_formula += f" ~x{position} &"
        elif int(digit) is 1:
            boolean_formula += f" x{position} &"
        else:
            print("Something has gone wrong")

        position += 1
    boolean_formula = boolean_formula[:-1]
    print(expr(boolean_formula))

# even and prime arrays
even = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
prime = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# print(number_to_boolean_formula(3));
number_to_boolean_formula(3);
