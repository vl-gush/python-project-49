import prompt
from random import randint


def engine(game, name: str, attempts: int = 3):
    while attempts:
        number = randint(0, 100)
        if game(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            attempts -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.""")
            print(f"Let's try again, {name}!""")
            break
    if attempts == 0:
        print(f"Congratulations, {name}!")
