

import math
import cmath
import random

def primary_school_quiz(flag, n):
    '''(number,number)
    Precondition: flag equals 0 or 1
    Helps the user practice solving subtraction or exponentiation problems. The paramater, 'n',
    is the number of problems that the user attempts to solve.
    If flag = 0, subtraction problems are presented.
    If flag = 1, exponentiation problems are presented.
    At the end of the quiz, the user's performance is evaluated and is
    given feedback based on the score.'''

    if flag == 0:
        print('You have selected subtraction problems. Let us begin!')
        final_score = 0
        score = 0
        total = n

        while n > 0:
            a = random.randint(0,9)
            b = random.randint(0,9)
            answer = b - a
            q = str(input(str(b) + ' - ' + str(a) + ' = '))
            if q == str(b - a):
                print('Correct!')
                score = score + 1
            else:
                print('Incorrect. The correct answer is ' + str(answer))
            n = n - 1
            if n == 0:
                final_score = (score / total)*100
                print(name,"you answered",score,"out of",total,"questions correctly")
                print("That is",final_score,"%")

                if final_score >= 90:
                    print("Congratulations, " + name + "! you'll probably get an A tomorrow.")
                    print("Now go eat dinner and get some sleep.")
                elif 70 <= final_score < 90:
                    print("You did well,",name,"but I know you can do a lot better.")
                elif final_score < 70:
                    print("I think you need some more practice, " + name + ".")
                    
    elif flag == 1:
        print('you have selected exponentiation problems. Let us begin!')

    final_score = 0
    score = 0
    total = n

    while n > 0:
        a = random.randint(0,9)
        b = random.randint(0,9)
        answer = a**b

        q = str(input(str(a) + '**' + str(b) + ' = '))
        if q == str(a**b):
            print('Correct!')
            score = score + 1
        else:
            print('Incorrect. The correct answer is ' + str(answer))
        n = n - 1
        if n == 0:
                final_score = (score / total)*100
                print(name,"you answered",score,"out of",total,"questions correctly")
                print("That is",final_score,"%")

                if final_score >= 90:
                    print("Congratulations, " + name + "! you'll probably get an A tomorrow.")
                    print("Now go eat dinner and get some sleep.")
                elif 70 <= final_score < 90:
                    print("You did well,",name,"but I know you can do a lot better.")
                elif final_score < 70:
                    print("I think you need some more practice, " + name + ".")
        

def high_school_eqsolver(a,b,c):
    '''(int,int,int)->str
    Takes the paramaters a,b,c and determines the roots of the quadratic equation.
    It will do this by calculating the discriminant and then return the roots
    according to the results of the discriminat.'''

    if a == 0:
        print("WARNING: If a equals 0, a divide by 0 error will occur!")
        print("Restarting program.")
    
    else:
        d = b**2 - 4*a*c #discriminant
        if d == 0:
            root = ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)
            print('The quadratic equation ' + str(a) + ' x^2 +' + str(b) + 'x + ' + str(c))
            print('has one real root:')
            print(root)
        if d > 0:
            root1 = ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)
            root2 = ((-b) - ((math.sqrt((b*b) - 4*a*c))))/(2*a)
            print('The quadratic equation ' + str(a) + 'x^2 ' + str(b) + 'x + ' + str(c))
            print('has two real roots:')
            print(root1,'and',root2)
        if d < 0:

            root1 = ((-b) + ((cmath.sqrt((b*b) - 4*a*c))))/(2*a)
            root2 = ((-b) - ((cmath.sqrt((b*b) - 4*a*c))))/(2*a)
            print('The quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))
            print('has the following complex roots: ')
            print(root1,'and',root2)


# main

print("*"*58)
print("*" + ' '*56 + "*")
print("*__Welcome to the Math Quiz Generator / Equation Solver__*")
print("*" + ' '*56 + "*")
print("*"*58)

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    def primary_menu():
        '''(none)->(none)
        Acts as the menu for the primary school quiz. It will ask for what
        operation the user would like to practice and how many questions they
        would like to have. It will then call the primary_school_quiz(flag,n)
        function'''
        flag = 3
        n = -1 #flag = 3 and n = -1 to activate while loop
        print("You have selected the primary school quiz program.")

        while flag != 0 and flag != 1:
            flag = int(input("Input '0' for subtraction or '1' for exponentiation: "))
        if flag == 0 or flag == 1:
            while n < 0:
                n = int(input("How many questions would you like on your quiz?: "))

        primary_school_quiz(flag,n)

    print("*"*56)
    print("*" + ' '*54 + "*")
    print("*__Welcome to the quiz generator for primary students__*")
    print("*" + ' '*54 + "*")
    print("*"*56)

    primary_menu()

elif status=='2':
    def secondary_menu():
        '''(none) -> (None)
        Acts as the menu for the high school quadratic equation solver. It will
        ask for the coefficients of a, b, and c and then will call the
        high_school_eqsolver(a,b,c) function to compute the results'''
        a = 0
        b = 0
        c = 0

        while type(a) != type(float):
            a = input('Input a coefficient for a: ')
            try:
                a = float(a)
                if a.is_integer() == True:
                    a = int(a)
                break
            except ValueError:
                print('Invalid input. Please input a number')

        while type(b) != type(float):
            b = input('Input a coefficient for b: ')
            try:
                b = float(b)
                if b.is_integer() == True:
                    b = int(b)
                break
            except ValueError:
                print('Invalid input. Please input a number')

        while type(c) != type(float):
            c = input('Input a coefficient for c: ')
            try:
                c = float(c)
                if c.is_integer() == True:
                    c = int(c)
                break
            except ValueError:
                print('Invalid input. Please input a number')


        high_school_eqsolver(a,b,c)
        
        
    print("*"*46)
    print("*" + ' '*44 + "*")
    print("*__Welcome to the quadratic equation solver__*")
    print("*" + ' '*44 + "*")
    print("*"*46)
    #welcome msg
    
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        question = question.lower()

        if question != "yes":
            flag=False
        else:
            print("Good choice!")
            secondary_menu()
                    
 
else:
    print("The program is not intended for you. The program will now terminate.")

print("Good bye "+name+"!")