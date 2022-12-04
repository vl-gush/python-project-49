import random


def gcd() -> int:
    """Returns the greatest common divisor of two random numbers
    """
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    print(f"Question: {num1} {num2}")
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2
