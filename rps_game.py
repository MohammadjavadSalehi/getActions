import random

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
            user_choice == 'paper' and computer_choice == 'rock' or \
            user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
    else:
        print("You lose!")

def run_game():
    play_again = 'yes'
    while play_again == 'yes':
        user_choice = input("Choose rock, paper, or scissors: ")
        play_game(user_choice)
        play_again = input("\nDo you want to play again? (yes/no): ")
    print("Thanks for playing!")

run_game()