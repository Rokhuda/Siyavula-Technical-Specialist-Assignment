import math
import random

def generate_random_quadratic_formulas():
    for i in range(0,10):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        c = random.randint(-10,10)

        if a == 1 and b == 1:
            print(f"y = x^2 + x + {c}")
        if a == 1:
            print(f"y = x^2 + {b}x + {c}")
        if a == 0 or b == 0:
            return
         
        print(f"y = {a}x^2 + {b}x + {c}")

generate_random_quadratic_formulas()