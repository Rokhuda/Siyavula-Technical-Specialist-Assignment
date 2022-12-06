class QuadraticSolver:
    def __init__(self, A,B,C):
        self.A = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        self.B = random.randint(-10, 10)
        self.C = random.randint(-10, 10)

    
    def calculate_root(a,b,c):
        return ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)

    def calculate_descriminant(a,b,c):
        return b * b - 4 * a * c
    
    def generate_quadratic_equation():
        pass







def _generate_quadratic_eq():
    pass
def _generate_a_set_of_quad_eq():
    pass



