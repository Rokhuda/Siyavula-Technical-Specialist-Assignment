import random


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
    """
    Generating a real root quadratic equation 
    """
    a = generate_constant_a()
    b = generate_constant_b()
    c = generate_constant_c()

    # The value of the descriminnt will determine if the quadratic equation will be a real root
    descriminant = b * b - 4 * a * c
    if descriminant >= 0:
        return f"{a}x^2 + {b}x + {c} = 0"
    else:
        # if the descriminant is less that 0 -> not a real root, call the function again an regenerate new a,b,c values
        return generate_real_root_quadratic_equation()


def set_of_ten_random_real_root_quadratic_equations():
    new_set = {i: generate_real_root_quadratic_equation() for i in range(1, 11)}
    return new_set


def print_ten_random_real_root_quadratic_equations():

    for i, (key, value) in enumerate(
        set_of_ten_random_real_root_quadratic_equations().items()
    ):

        print(f"{key}: {value}")

print(f"Real root Quadratic Equations: ")

print_ten_random_real_root_quadratic_equations()
