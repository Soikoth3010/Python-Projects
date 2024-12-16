import random
from unittest.mock import right

Operators = ["+", "-", "/", "*"]
MIN_Operand = 3
MAX_Operand = 12

def generate_problem():
    left = random.randint(MIN_Operand, MAX_Operand)
    right = random.randint(MIN_Operand, MAX_Operand)
    operator = random.choice(Operators)

    expression = str(left)+ " " + operator + " " +str(right)
    print(expression)
    return expression

generate_problem()