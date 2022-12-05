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


# rename funtion + root solution


def generate_quadratic_equation():
    """
    a*x^2+b*x+c = 0
    """
    a=gen_a()
    b=gen_b()
    c=gen_c()

    descriminant = b * b - 4 * a * c
    new_line = '\n'
    eq = f"{a}x^2 + {b}x + {c} = 0"

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

  
print("WARNING: If a equals 0, a divide by 0 error will occur!")
print()   
for i in range(1,11):
    print(f'{i}: {generate_quadratic_equation()}')



generate_quadratic_equation()