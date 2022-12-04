import random
from operator import add, sub, mul

DESCRIPTION = "What is the result of the expression?"

OPERATORS = {
    "+": add,
    "-": sub,
    "*": mul,
}


def calc() -> tuple:
    num1 = random.randint(0, 50)
    num2 = random.randint(0, 50)
    operator = random.choice(list(OPERATORS))
    question = f"Question: {num1} {operator} {num2}"
    answer = OPERATORS[operator](num1, num2)
    return question, str(answer)
