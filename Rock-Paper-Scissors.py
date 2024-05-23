#This is going to be a game of rock, paper, scissors

import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    rounds = 5
    user_score = 0
    computer_score = 0
    ties = 0

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            print("You win this round!")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a tie!")
            ties += 1
    
    print("\nGame Over!")
    print(f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}\nTies: {ties}")

if __name__ == "__main__":
    play_game()
