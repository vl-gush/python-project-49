import random

DESCRIPTION = 'Enter "yes" if the number is even, otherwise enter "no".'


def even():
    number = random.randint(0, 100)
    question = f"Question: {number}"
    answer = "yes" if number % 2 == 0 else "no"
    return question, answer
