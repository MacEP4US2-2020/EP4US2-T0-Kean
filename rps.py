import random 

options = ['r','p','s']

def computer_turn():
    computer = options[random.randint(0,2)]
    print("The computer chooses:", computer)
    return computer

def user_turn():
    user_choice = input("Select one of 'r', 'p', 's'")
    if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
        return user_choice
    else:
        print("Please try again, that's an invalid choice.")

def who_wins(player, computer):
    if (player == 'r' and computer == 's'):
        print("The player wins")
    elif (player == 'p' and computer == 'r'):
        print("The player wins")
    elif (player == 's' and computer == 'p'):
        print("The player wins")
    elif (player == computer):
        print("It's a tie!")
    else:
        print("The computer wins!")

def game_round():
    player = user_turn()
    computer = computer_turn()
    who_wins(player, computer)

game_round()