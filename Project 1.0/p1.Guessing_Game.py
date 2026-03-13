import random

print("Welcome to the Number Guessing Game")

print("Choose difficulty:")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")

choice = input("Enter choice: ")

if choice == "1":
    number = random.randint(1, 10)
elif choice == "2":
    number = random.randint(1, 50)
else:
    number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Correct! You guessed it in", attempts, "attempts.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

print("Thanks for playing!")
