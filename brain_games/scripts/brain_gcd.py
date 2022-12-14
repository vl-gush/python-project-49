from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.gcd import gcd, DESCRIPTION


def main():
    name = welcome_user()
    print(f"\n{DESCRIPTION}\n")
    engine(gcd, name)


if __name__ == "__main__":
    main()
