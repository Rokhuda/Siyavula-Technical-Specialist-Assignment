import random

def gen_a():
    'a cannot be zero'
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return a

def gen_b():
    b = random.randint(-10, 10)
    return b
def gen_c():
    c = random.randint(-10, 10)
    return c


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

    for i, (key, value) in enumerate(set_of_ten_random_real_root_quadratic_equations().items()):

        print(f'{key}: {value}')


print_ten_random_real_root_quadratic_equations()