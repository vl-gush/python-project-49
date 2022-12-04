from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.even import even, DESCRIPTION


def main():
    name = welcome_user()
    print(f"\n{DESCRIPTION}\n")
    engine(even, name)


if __name__ == "__main__":
    main()
