import random

options = ("rock", "paper", "scissors")
is_running = True

while is_running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    
    # if not input("Play again? (y/n): ").lower() == "y":
    #     is_running = False

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        is_running = True
    else:
        is_running = False

print("Thanks for playing!")

