import random
'''
properties of quadratic equations-
- a cannot be zero (otherwise function is undefined)
- b and/or c can be zero
- a,b,c can be any random integer from negative infinity to positive infinity
- a,b,c take the sign of the operator


'''

ntive_inf = float('-inf')
ptive_inf = float('inf')


def gen_a():
   
    a = random.choice([random.randint(-10, -1),random.randint(1, 10)])
    return f'{a}x^2'

def gen_b():
    b = random.randint(-10, 10)
    if b == 0:
        result = ''
    elif b > 0 :
        result = f'+ {b}x'

    else:
        result = f'{b}x'
    return  result

def gen_c():
    c = random.randint(-10, 10)
    if c == 0:
        result = ''
    elif c > 0 :
        result = f'+ {c}'

    else:
        result = f'{c}'
    return  result



def generate_quadratic_equation():
    '''
    a*x^2+b*x+c = 0
    '''
    
    eq = f"{gen_a()}{gen_b()}{gen_c()} = 0"

    return eq

print(f'Quadratic Equations')
for i in range(1,11):
    print(f'{i}: {generate_quadratic_equation()}')

        

generate_quadratic_equation()