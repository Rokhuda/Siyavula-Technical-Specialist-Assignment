
import random
import math
from xmlrpc.client import boolean

'''
from sympy import symbols
from sympy.abc import x

'''

def gen_a():
    a = random.choice([random.randint(-10, -1),random.randint(1, 10)])
    return f'{a}x^2'

def gen_b():
    b = random.randint(-10, 10)
    if b == 0:
        # result = '0'
        result = 0

    elif b > 0 :
        # result = f'+ {b}x'
        result = b

    else:
        # result = f'{b}x'
        result = b

    return  result

def gen_c():
    c = random.randint(-10, 10)
    if c == 0:
        # result = '0'
        result = 0

    elif c > 0 :
        # result = f'+ {c}'
        result = c


    else:
        # result = f'{c}'
        result = c

    return  result


        

# Function checks if the generated constants produce a real root quadratic equation by returning a boolean
# def is_real_roots(a, b, c) -> boolean:
#     if type(a) != int and type(b) != int and type(c) != int:
#         return False
#     else:
#         if a == 0:
#             return False
#         descriminant = b**2 - 4 * a * c

#         if descriminant > 0:
#             return True
#         elif descriminant == 0:
#             return True
#         else:
#             return False


# rename funtion + root solution
# def randomly_arranged_equaton():
    
#     eq1 = f"{a}{b}{c} = 0"
#     eq2 = f"{a}{b} = {c}"
#     eq3 = f"{b} = {c}{a}"
#     eq4 = f"{b}{a} = {c}"
#     eq5 = f"{b}{c} = {a}"

#     eq_list = [eq1,eq2,eq3,eq4,eq5]
#     # choice will choose a random item in the sequence
#     return random.choice(eq_list)



def generate_quadratic_equation():
    """
    a*x^2+b*x+c = 0
    """
    a=gen_a()
    b=gen_b()
    c=gen_c()

    descriminant = b * b - 4 * a * c
    new_line = '\n'

   

    eq = randomly_arranged_equaton()


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

  
# print("WARNING: If a equals 0, a divide by 0 error will occur!")
# print()   
# for i in range(1,11):
#     print(f'{i}: {generate_quadratic_equation()}')



print(generate_quadratic_equation())



# randominze quadratic equation arrangement




# def input_your_answers(root1,seperator,root2):
#     ''' 1;1'''
#     root1 = int(input('root1'))
#     root2 = int(input('root2'))
#     seperator = input(';')
#     if type(root1) != int and type(root1) and seperator!= ';':
#         raise ValueError('Enter digits seperated by a semicolon (;)')
#     else:
#         # if 
#         'check if generated quadratic match solution else try again'


# def solve_the_equestion_2x_value():
#     ''' x = 1 or x = 3'''
#     print(f'x ={root1} or x ={root2}')


# def solve_the_equestion_1x_value(a,b,c):

#     '''
#     x = val1 +- square_root(val2) / val3
#     '''
#     val1 = (-b)
#     val2 = b*b - 4*a*c
#     val3 = 2*a
    
#     print(f'({val1}) +- ((math.sqrt({val2}))/({val3}))')


# def arrange_quad_eq_in_standard_form():
#     print('randomly arranged quad eq')
#     print('quad eq')


# def function_remove_fractions():

#     pass


# def quad_eq_to_solve():
#     pass



