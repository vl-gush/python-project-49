import random
from operator import add, sub, mul

OPERATORS = {
    "+": add,
    "-": sub,
    "*": mul,
}


def calc() -> int:
    """Returns the result of a random operation from the OPERATORS dictionary \
on two random numbers.
    """
    num1 = random.randint(0, 50)
    num2 = random.randint(0, 50)
    operator = random.choice(list(OPERATORS))
    print(f"Question: {num1} {operator} {num2}")
    return OPERATORS[operator](num1, num2)
