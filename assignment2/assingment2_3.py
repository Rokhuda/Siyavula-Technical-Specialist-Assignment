import random
import math

def gen_a():
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return a

def gen_b():
    b = random.randint(-10, 10)
    return b
def gen_c():
    c = random.randint(-10, 10)
    return c

def calculate_descriminant(a,b,c):
    return b * b - 4 * a * c

def calculate_root(a,b,c):
    return ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)



# 2.1

def generate_quadratic_equation():
    '''
    a*x^2+b*x+c = 0
    '''
    a=gen_a()
    b=gen_b()
    c=gen_c()
    eq = f"{a}x^2 + {b}x + {c} = 0"
    return eq


def set_of_ten_quadratic_equation():
    new_set = {i: generate_quadratic_equation() for i in range(1,11)}
    return new_set


def print_ten_quadratic_equation():
    print(f'Quadratic Equations')
    for i, (key, value) in enumerate(set_of_ten_quadratic_equation().items()):
        print(f'{key}: {value}')


print_ten_quadratic_equation()


# 2.2
def generate_real_root_quadratic_equation():
    """
    a*x^2+b*x+c = 0
    """
    a=gen_a()
    b=gen_b()
    c=gen_c()
    descriminant = b * b - 4 * a * c
    if descriminant >= 0:
        return f"{a}x^2 + {b}x + {c} = 0"
    else:
        # if the descriminant is less that 0 -> not a real root, call the function again an regenerate new a,b,c values
        return generate_real_root_quadratic_equation()

def set_of_ten_random_real_root_quadratic_equations():
    new_set = {i: generate_real_root_quadratic_equation() for i in range(1,11)}
    return new_set


def print_ten_random_real_root_quadratic_equations():
    print(f'Quadratic Equations')

    for i, (key, value) in enumerate(set_of_ten_random_real_root_quadratic_equations().items()):

        print(f'{key}: {value}')


# print_ten_random_real_root_quadratic_equations()



# 2.3
def generate_real_root_quadratic_equation_with_solution():
    """
    a*x^2+b*x+c = 0
    """
    a=gen_a()
    b=gen_b()
    c=gen_c()

    descriminant = calculate_descriminant(a,b,c)
    
    new_line = '\n'
    
    eq = f"{a}x^2 + {b}x + {c} = 0"

    if descriminant == 0:
        root = calculate_root(a,b,c)
        return f'The quadratic equation : {new_line} {eq} {new_line}Has a Descriminent of : {new_line} {descriminant} {new_line}Has one real root: x = {root}'
      
    if descriminant > 0:
        eq = f"{a}x^2 + {b}x + {c} = 0"
        root1 = calculate_root(a,b,c)
        root2 = calculate_root(a,b,c)
       
        return f'The quadratic equation : {new_line} {eq} {new_line}Has a Descriminent of : {new_line} {descriminant} {new_line}Has two real roots : {new_line} x = {root1} {new_line} x = {root2}'
    else:
        # if the descriminant is less that 0 -> not a real root, call the function again an regenerate new a,b,c values
        return generate_real_root_quadratic_equation_with_solution()


def print_generate_real_root_quadratic_equation_with_solution():
    print("Note: If the value of a equals 0, a divide by 0 error will occur!")
    print()   
    print(generate_real_root_quadratic_equation_with_solution())


# print_generate_real_root_quadratic_equation_with_solution()