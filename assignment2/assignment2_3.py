import random
import math


def generate_constant_a():
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return a


def generate_constant_b():
    b = random.randint(-10, 10)
    return b


def generate_constant_b():
    c = random.randint(-10, 10)
    return c

def generate_constant_a():
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    return a


def generate_constant_b():
    b = random.randint(-10, 10)
    return b


def generate_constant_b():
    c = random.randint(-10, 10)
    return c



def calculate_descriminant(a, b, c):
    return b * b - 4 * a * c


def calculate_root1(a, b, c):
    return ((-b) + ((math.sqrt((b * b) - 4 * a * c)))) / (2 * a)

def calculate_root2(a, b, c):
    return ((-b) - ((math.sqrt((b * b) - 4 * a * c)))) / (2 * a)


def generate_real_root_quadratic_equation_with_solution():
   
    a = generate_constant_a()
    b = generate_constant_b()
    c = generate_constant_c()

    descriminant = calculate_descriminant(a, b, c)

    new_line = "\n"

    equation = f"{a}x^2 + {b}x + {c} = 0"

    if descriminant == 0:
        root = calculate_root1(a, b, c)
        return f"The quadratic equation : {new_line} {equation} {new_line}Has a Descriminent of : {new_line} {descriminant} {new_line}Has one real root: x = {root}"

    if descriminant > 0:
        equation = f"{a}x^2 + {b}x + {c} = 0"
        root1 = calculate_root1(a, b, c)
        root2 = calculate_root2(a, b, c)

        return f"The quadratic equation : {new_line} {equation} {new_line}Has a Descriminent of : {new_line} {descriminant} {new_line}Has two real roots : {new_line} x = {root1} {new_line} x = {root2}"
    else:
        # if the descriminant is less that 0 -> not a real root, call the function again an regenerate new a,b,c values
        return generate_real_root_quadratic_equation_with_solution()


def print_generate_real_root_quadratic_equation_with_solution():
    print("Note: If the value of a equals 0, a divide by 0 error will occur!")
    print()
    print(generate_real_root_quadratic_equation_with_solution())


print_generate_real_root_quadratic_equation_with_solution()
