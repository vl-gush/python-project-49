import math
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    number = random.randint(2, 100)
    question = f"Question: {number}"
    answer = "yes" if is_prime(number) else "no"
    return question, answer


def is_prime(number):
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            return False
    return True
