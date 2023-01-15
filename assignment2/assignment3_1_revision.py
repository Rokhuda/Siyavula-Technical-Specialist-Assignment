import random
import math

'''
Solution to a specific version of one instance
Every time this script runs, one version of the solution will be generated

This script works in a perfect worrld wher a human will input root integers and a semicolon as a seperator if math domain errors and other errors do not occur
Rerun script until a Quadratic equatipn that does not raise errors is submitted
'''

'''
REVIEW FEEDBACK
N.B fOCUS ON GENERATING CONSTANTS
1. Run code to ensure that the library works
2. Cater for positive and negatives while generating constants
3. Create libraries/ make code reusable
4. Missing X on the quadratic equations
5. Ensure that the constants are being regenerated
6. Error in the wrong discriminant
7. Ensure that the quadratic equations are equivalent
8. Somethig about the roots and the discriminat
9. Something about the user input not expected
10. The expectation of all this strings

'''


def generate_constant_a():
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return a


def generate_constant_b():
    b = random.randint(-10, 10)
    return b


def generate_constant_c():
    c = random.randint(-10, 10)
    return c



def calculate_descriminant(a, b, c):
    return b * b - 4 * a * c


def calculate_root1(a, b, c):
    return ((-b) + ((math.sqrt((b * b) - 4 * a * c)))) / (2 * a)


def calculate_root2(a, b, c):
    return ((-b) - ((math.sqrt((b * b) - 4 * a * c)))) / (2 * a)




def clean_constant_a(a):
    if a == 1:
        results = "x^2 "
    elif a == -1:
        results = "-x^2 "
    else:
        results = f"{a}x^2 "
    return results


def clean_constant_b(b):
    if b == 0:
        result = ""
    
    elif b == 1:
        result = f" x"

    elif b == -1:
        result = " -x"

    elif b > 1:
        result = f"+ {b}x"

    else:
        result = f" {b}x"

    return result


def clean_constant_c(c):
    if c == 0:
        result = ""
    elif c > 0:
        result = f" + {c}"

    else:
        result = f" {c}"
    return result




def generate_real_root_quadratic_equation():
    A = generate_constant_a()
    B = generate_constant_b()
    C = generate_constant_c()
    DESCRIMINENT = calculate_descriminant(A, B, C)

    a_string = f"{clean_constant_a(A)}"
    b_string = f"{clean_constant_b(B)}"
    c_string = f"{clean_constant_c(C)}"


    STANDARD_QUADRATIC_EQUATION = f"{a_string} {b_string} {c_string} = 0"

    eq2 = f"{a_string} {b_string} = {c_string}"
    eq3 = f"{b_string} = {a_string} {c_string}"

    eq5 = f"{b_string} {c_string} = {a_string}"
    eq_list = [STANDARD_QUADRATIC_EQUATION, eq2, eq3, eq5]
    quadratic_equation = random.choice(eq_list)

    if quadratic_equation[-2:] == '= ':
        quadratic_equation = quadratic_equation + '0'
    if quadratic_equation[:2] == ' =' or quadratic_equation[:3] == '  =':
        quadratic_equation = '0' + quadratic_equation 

    if quadratic_equation.startswith('+'):
        quadratic_equation = quadratic_equation[1:]

    if "  " in quadratic_equation:
        quadratic_equation =  quadratic_equation.replace("  ", " ")

    if DESCRIMINENT == 0:
        return quadratic_equation 
    else:
        return generate_real_root_quadratic_equation()


print(generate_real_root_quadratic_equation())
