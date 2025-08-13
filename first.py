import random

print("Hello! Welcome to Rock, Paper, Scissors.")

while True:
    a = int(input("Enter rock (1), paper (2), or scissors (3): "))
    b = random.choice([1, 2, 3])

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {choices[a]}")
    print(f"Computer chose: {choices[b]}")


    if a == b:
        print("It's a tie!")
    elif (a == 1 and b == 3) or (a == 3 and b == 2) or (a == 2 and b == 1):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
