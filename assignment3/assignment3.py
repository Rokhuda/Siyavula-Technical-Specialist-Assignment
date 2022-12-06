
import random
import math
from xmlrpc.client import boolean

'''
from sympy import symbols
from sympy.abc import x

'''

def gen_a():
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return a

def gen_b():
    b = random.randint(-10, 10)
    return b

def gen_c():
    c = random.randint(-10, 10)
    return c


def generate_quadratic_equation():

    a=gen_a()
    b=gen_b()
    c=gen_c()

    descriminant = b * b - 4 * a * c
    new_line = '\n'
    standard_eq = f"{a}x^2 + {b}x + {c} = 0"
    eq2 = f"{a}x^2 {b}x = {c}"
    eq3 = f"{b}x = {c}{a}x^2"
    eq4 = f"{b}{a}x^2 = {c}"
    eq5 = f"{b}{c} = {a}x^2 "

    eq_list = [standard_eq,eq2,eq3,eq4,eq5]
    # choice will choose a random item in the sequence
    quad_eq = random.choice(eq_list)

    if descriminant == 0:
        root = ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)
        return f'The quadratic equation : {eq} {new_line} Has a Descriminent of {descriminant} {new_line}Has one real root: {root}'
      
    if descriminant > 0:
        eq = f"{a}x^2 + {b}x + {c} = 0"
        root1 = ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)
        root2 = ((-b) - ((math.sqrt((b*b) - 4*a*c))))/(2*a)
        return f'The quadratic equation : {eq} {new_line} Has a Descriminent of {descriminant} {new_line}Has two real roots: {new_line} {root1} {new_line} {root2}'
    else:
        # if the descriminant is less that 0 -> not a real root, call the function again an regenerate new a,b,c values
        return generate_quadratic_equation()





# sting1
def solve_the_following_quadratic_equation():
    return quad_eq

# string2
def remove_the_fractions_from_equation():
    generate_quadratic_equation()

    factorise = Factor().FactorQuad(a, b, c)

    if factorise == False:
        return 'equation does not need to be factorised'
    else:
        return factorise



# string3
def arrange_equation_in_standard_form():
    eq = solve_the_following_quadratic_equation()
    def _rearranged():
        pass

    if eq == standard_eq:
        return eq
    else:
        return _rearranged()

# string4

def reduce_the_equation():
    
    '''
    x = val1 +- square_root(val2) / val3
    '''
    val1 = (-b)
    val2 = b*b - 4*a*c
    val3 = 2*a
    
    return f'({val1}) +- ((math.sqrt({val2}))/({val3}))'


# string5
def print_roots(a,b,c):

    return ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)

# string6
def input_your_answers(root1,seperator,root2):
    ''' 1;1'''
    root1 = int(input('root1'))
    root2 = int(input('root2'))
    seperator = input(';')
    if type(root1) != int and type(root1) and seperator!= ';':
        return f'Enter digits seperated by a semicolon (;){input_your_answers(root1, seperator, root2)}'
    else:
        return 'Nice'



print(generate_quadratic_equation())
print(remove_the_fractions_from_equation())
print(arrange_equation_in_standard_form())
print(reduce_the_equation())
print(print_roots())
print(input_your_answers())
