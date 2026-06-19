import random

user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors Game")
    print("Enter rock, paper, or scissors")

    user = input("Your choice: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice!")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Score")
    print("User:", user_score)
    print("Computer:", computer_score)

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break