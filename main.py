
import random


def get_guess():
    """Get a valid number from the player."""
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game():
    """Run one round of the guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")

        elif guess > secret_number:
            print("📈 Too high!")

        else:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You got it in {attempts} attempt(s).")
            break


def main():
    """Start the game and handle replay."""
    print("================================")
    print("       🎯 GUESSING GAME")
    print("================================")

    while True:
        play_game()

        while True:
            again = input("\nDo you want to play again? (y/n): ").lower().strip()

            if again in ("y", "n"):
                break

            print("Please enter 'y' for yes or 'n' for no.")

        if again == "n":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()

