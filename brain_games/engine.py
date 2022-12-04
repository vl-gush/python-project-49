import prompt


def engine(game, name: str, attempts: int = 3):
    while attempts:
        correct_answer = game()
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            attempts -= 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. \
Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    if attempts == 0:
        print(f"Congratulations, {name}!")
