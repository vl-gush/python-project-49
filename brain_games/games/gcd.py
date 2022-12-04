import random

DESCRIPTION = "Enter the largest common divisor of two numbers"


def gcd():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = f"Question: {num1} {num2}"
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    answer = num1 + num2
    return question, str(answer)
