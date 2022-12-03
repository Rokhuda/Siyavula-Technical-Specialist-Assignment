import random

# https://problemsolvingwithpython.com/10-Symbolic-Math/10.05-Equations/
from sympy import symbols, Eq


class QuadraticEquations:
    """
    This class generates a lis of 10 random quadratic equation
    """

    def __init__(self):
        x = symbols("x")
        self.a = random.randint(-10, 10) * x
        self.b = random.randint(-10, 10) * x
        self.c = random.randint(-10, 10)

    def generate_quadratic_equation(self):
        quadratic_equation = f"{self.a}^2+{self.b}+{self.c}=0"
        # print(quadratic_equation)
        return quadratic_equation

    def generate_10_random_quadratic_equations(self):
        quadratic_equations = []

        for i in range(10):
            i +=1
            quadratic_equations.append({self.generate_10_random_quadratic_equations()})
        return quadratic_equations

    # def display_generated_equation(self):

    #     for quad_equation in self.generate_10_random_quadratic_equations():
    #         print(f'Quadratic Equation : {self.quad_equation}')


thing1 = QuadraticEquations()
print(thing1.generate_quadratic_equation())
