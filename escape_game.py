import random

secret_number = random.randint(1, 20)
attempts = 5

print("=== Mystery Number Escape ===")
print("Guess the secret number to escape the system.")
print("You have 5 attempts.\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("\nAccess granted. You escaped!")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("\nSystem locked. The number was:", secret_number)
