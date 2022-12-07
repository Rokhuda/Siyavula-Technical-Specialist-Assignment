
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


def generate_real_root_quadratic_equation():

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

    if descriminant >= 0:
         return quad_eq
    else:
        return generate_real_root_quadratic_equation()



# sting1
def solve_the_following_quadratic_equation():
    quad_eq = generate_real_root_quadratic_equation()
    return quad_eq

# string2
# factorise
def remove_the_fractions_from_equation():
    a=gen_a()
    b=gen_b()
    c=gen_c()
    eq = solve_the_following_quadratic_equation()
    

    # def _factorise():
    '''
    If the coeffiecient of a is greater than 0 we use grouping method to factorise
    '''
    if a == 1:
        # sum product
        return eq
    
        # grouping
    eq = f'{a}x(x+{c}) - 1(x + {c}) =0'
    return eq
        


# string3
def arrange_equation_in_standard_form():
    a=gen_a()
    b=gen_b()
    c=gen_c()
    standard_eq = f"{a}x^2 + {b}x + {c} = 0"
    eq = generate_real_root_quadratic_equation()

    new_line = '\n'
    if eq != standard_eq:
        return f'{eq}{new_line}{standard_eq}'
    return standard_eq

# string4

def reduce_the_equation():
    a=gen_a()
    b=gen_b()
    c=gen_c()
    
    '''
    x = val1 +- square_root(val2) / val3
    '''
    val1 = (-b)
    val2 = b*b - 4*a*c
    val3 = 2*a
    
    return f'({val1}) +- ((math.sqrt({val2}))/({val3}))'


# string5
def print_roots():
    a=gen_a()
    b=gen_b()
    c=gen_c()
    root_1 = int(((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a))
    root_2 =  int(((-b) - ((math.sqrt((b*b) - 4*a*c))))/(2*a))
    return f'{root_1} ; {root_2}'



# string6
def input_your_answers():
    ''' 1;1'''
    a=gen_a()
    b=gen_b()
    c=gen_c()
    root_1 = int(((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a))
    root_2 =  int(((-b) - ((math.sqrt((b*b) - 4*a*c))))/(2*a))

    root1 = int(input('Input root1 : '))
    seperator = input('seperator')

    root2 = int(input('Input root2 : '))

    your_answer = f'{root1}{seperator}{root1}'
    

    if type(root1) == int and type(root2) == int and seperator == ';':
        if root1 == root_1 and root2 == root_2: 
            return f'{print_roots()}'
            
        return f'Try again : {your_answer}'
    else:
        raise ValueError('Enter digits seperated by s semicolon (;)') 
    
    return f'{root_1}{seperator}{root_1}'



print(generate_real_root_quadratic_equation())
print(remove_the_fractions_from_equation())
print(arrange_equation_in_standard_form())
print(reduce_the_equation())
print(print_roots())
print(input_your_answers())
