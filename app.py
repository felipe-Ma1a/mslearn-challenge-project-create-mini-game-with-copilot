# create a rock, paper, scissors game
# the player can choose one of the three options rock, paper or scissors, and should be warned if they choose an invalid option
# In every round, the player need to choose one of the options on the list and be warned if he wins, loses or ties with the opponent
# In the end of every round, the player can choose to play again
# Show the player's score in the end of the game
# The minigame needs to handle user inputs, putting them in lowercase and telling the user if the input is invalid

import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    opponent_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        opponent_choice = random.choice(options)
        print(f"Opponent chooses {opponent_choice}.")

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
             (player_choice == 'paper' and opponent_choice == 'rock') or \
             (player_choice == 'scissors' and opponent_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            opponent_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Player score: {player_score}")
    print(f"Opponent score: {opponent_score}")

play_game()