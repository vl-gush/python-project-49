import random

DESCRIPTION = "What number is missing?"


def progression():
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    progression_length = random.randint(5, 10)
    index = random.randint(0, progression_length - 1)
    sequence = list(map(
        str,
        range(start, start + progression_length * step, step)
    ))
    answer = sequence[index]
    sequence[index] = ".."
    question = f"Question: {' '.join(sequence)}"
    return question, answer
