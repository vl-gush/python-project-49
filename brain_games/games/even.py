import random


def even() -> str:
    """Returns "yes" if the number is even, otherwise "no".
    """
    number = random.randint(0, 100)
    print(f"Question: {number}")
    return "yes" if number % 2 == 0 else "no"
