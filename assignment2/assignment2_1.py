import random

def generate_constant_a():
    '''
    The result has to be between -10 and 10 and ensure that a is not zero. 
    '''
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return f"{a}x^2"


def generate_constant_b():
    b = random.randint(-10, 10)
    if b == 0:
        result = ""
    elif b > 0:
        result = f"+ {b}x"

    else:
        result = f"{b}x"
    return result


def generate_constant_c():
    c = random.randint(-10, 10)
    if c == 0:
        result = ""
    elif c > 0:
        result = f" + {c}"

    else:
        result = f" {c}"
    return result


def generate_quadratic_equation():
    """
    Generating one quadratic equation 
    """

    equation = f"{generate_constant_a()} {generate_constant_b()} {generate_constant_c()} = 0"
    return equation


def set_of_ten_quadratic_equations():
    '''
    Creating a set of ten quadratic equadion
    '''
    new_set = {i: generate_quadratic_equation() for i in range(1, 11)}
    return new_set


def print_ten_generate_quadratic_equations():
    for i, (key, value) in enumerate(set_of_ten_quadratic_equations().items()):
        print(f"{key}: {value}")


print(f"Quadratic Equations: ")
print_ten_generate_quadratic_equation()
