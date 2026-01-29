import random

print("Welcome to Number Guessing Game \nYou have 7 Chances to Guess Correct Answer.")

lives = 7
tries = 0
try:
    bound_A = int(input('Enter Bound A Number: '))
    bound_B = int(input("Enter Bound B Number: "))
    computer_generated = random.randint(bound_A, bound_B)
    while True:
        print("")
        if lives > 0:
            print(f"Guess the number in between {bound_A} and {bound_B} Bounds.")
            guess = int(input("Guess the Generated Number: "))
            if guess not in range(bound_A, bound_B):
                print(f"Please Guess the number in selected Range {bound_A} and {bound_B}.")
                break
            else:
                if guess < computer_generated:
                    tries += 1
                    print("Try Again! You guessed too Low.")
                elif guess > computer_generated:
                    tries += 1
                    print("Try Again! You guessed too High.")
                else:
                    print("Congratulations!.")
                    print(f"You guessed in {tries}")
                    break
                lives -= 1
                print("No of lives remaining", lives)
        else:
            print("OPPS Better Luck Next Time!.")
            break
except ValueError:
    print("Enter Low to High")

