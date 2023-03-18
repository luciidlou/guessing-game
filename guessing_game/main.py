"""The project's main module for the guessing game."""

import random
from typing import Callable, Optional

__all__ = tuple()

# <editor-fold: Constants>

LOW: int = 1
HIGH: int = 20
MAX_GUESSES: int = 3

# </editor-fold: Constants>


def play_game() -> None:
    """Entry point for executing the guessing game."""

    tries: int = 1
    answer: int = random.randint(1, 20)
    prompt_user: str = f"Please choose a number between {LOW} and {HIGH}: "

    print("Welcome to the guessing game!! Lets play!")

    while tries <= MAX_GUESSES:
        print(f"You have {MAX_GUESSES - (tries - 1)} {'guesses' if tries != MAX_GUESSES else 'guess'} left.")
        user_guess = input(prompt_user)

        try:
            user_guess = int(user_guess)
        except ValueError as err:
            print(f"ERROR: {err} \n`{user_guess}` is not a valid integer!")
            continue

        if not LOW <= user_guess <= HIGH:
            print(f"Your guess must be between the numbers {LOW} and {HIGH}! Please guess again...")
            continue

        tries += 1

        if user_guess == answer:
            print("You guessed the right number! ✅")
            if not try_again(play_game):
                return
        else:
            lower_higher: str = "lower..." if user_guess > answer else "higher..."
            print(lower_higher)
            continue

    print(f"You lost 😢 \nThe correct answer was {answer}")
    try_again(play_game)


def try_again(func: Callable) -> Optional[bool]:
    """Asks the user if they want to try again."""

    user_input: str

    if not isinstance(func, Callable):
        raise TypeError(f"{func} is not of type `Callable`.")

    while True:
        user_input = input("Would you like to try again? (y/n)").lower()

        if user_input not in ("y", "n"):
            print(f"{user_input} is not an accepted input. Please choose either 'y' or 'n'...")
            continue

        if user_input == "y":
            play_game()

        if user_input == "n":
            print("Thanks for playing!")
            return False


if __name__ == "__main__":
    play_game()
