import math
import random
from calculate_roots import real_roots

def generate_quadratic_formula():
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)

    if a == 1 and b == 1:
        return f"y = x^2 + x + {c}"
    if a == 1:
        return f"y = x^2 + {b}x + {c}"
    if a == 0 or b == 0:
        return
        
    return f"y = {a}x^2 + {b}x + {c}"

def test_formula(list_of_formulas):
    a = None
    b = None
    c = None
    for i in list_of_formulas:
        remove_y = i.replace("y =", "")
        formula = remove_y.replace(" ", "").split("+")
        

        a_temp = formula[0]
        a_split = a_temp.split("x")
        a = int(a_split[0])
        
        b_temp = formula[1]
        b_split = b_temp.split("x")
        b = int(b_split[0])
        # print(b_split)

        if c == '':
            return
        c = int(formula[2])

    return {'a': a, 'b': b, 'c': c}

def generate_questions_with_constraints():
    arr = []


    while len(arr) < 10:
        generated_formula = generate_quadratic_formula()
        if generated_formula != None:
            arr.append(generated_formula)

            # print(test_formula(generated_formula))
            vals = test_formula(arr)

            # print(vals)

            is_real_root = real_roots(a = vals["a"], b = vals["b"], c = vals["c"])
            
            if is_real_root:
                print(generated_formula)


generate_questions_with_constraints()