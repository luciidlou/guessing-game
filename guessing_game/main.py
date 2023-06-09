"""The project's main module for the guessing game."""

import random
from typing import Callable, Optional
import os
from dotenv import load_dotenv

__all__ = tuple()

load_dotenv()

# <editor-fold: Constants>

USER: str = os.getenv("USER", "guest")
LOW: int = int(os.getenv("LOW", "1"))
HIGH: int = int(os.getenv("HIGH", "20"))
MAX_GUESSES: int = int(os.getenv("MAX_GUESSES", "3"))

# </editor-fold: Constants>


def play_game() -> None:
    """Entry point for executing the guessing game."""

    tries: int = 1
    answer: int = random.randint(LOW, HIGH)
    prompt_user: str = f"Please choose a number between {LOW} and {HIGH}: "

    print(f"Welcome, {USER}! Lets see if you can guess the right number!")

    while tries <= MAX_GUESSES:
        print(
            f"You have {MAX_GUESSES - (tries - 1)} "
            f"{'guesses' if tries != MAX_GUESSES else 'guess'} left."
        )
        guess = input(prompt_user)

        try:
            guess = int(guess)
        except ValueError as err:
            print(f"ERROR: {err} \n`{guess}` is not a valid integer!")
            continue

        if not LOW <= guess <= HIGH:
            print(
                f"Your guess must be between the numbers {LOW} and {HIGH}! "
                "Please guess again..."
            )
            continue

        tries += 1

        if guess == answer:
            print("You guessed the right number! ✅")
            if not play_again(play_game):
                return
        else:
            lower_higher: str = "lower..." if guess > answer else "higher..."
            print(lower_higher)
            continue

    print(f"You lost 😢 \nThe correct answer was {answer}")
    play_again(play_game)


def play_again(func: Callable) -> Optional[bool]:
    """Asks the user if they want to play again."""

    user_input: str

    if not isinstance(func, Callable):
        raise TypeError(f"{func} is not of type `Callable`.")

    while True:
        user_input = input("Would you like to play again? (y/n)").lower()

        if user_input not in ("y", "n"):
            print(
                f"{user_input} is not an accepted input. "
                "Please choose either 'y' or 'n'..."
            )
            continue

        if user_input == "y":
            play_game()

        if user_input == "n":
            print("Thanks for playing!")
            return False


if __name__ == "__main__":
    play_game()
