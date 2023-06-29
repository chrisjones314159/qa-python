import random
options = {1: "rock", 2: "paper", 3: "scissors"}
scores = {"playerW": 0, "compW": 0, "plays": 0, "draw": 0}
play = True

def game(choice):
    compChoice = random.randint(1, 3)
    if choice == compChoice:
        scores["plays"] = scores["plays"] + 1
        scores["draw"] = scores["draw"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Draw")

    elif choice == 1 and compChoice == 3:
        scores["plays"] = scores["plays"] + 1
        scores["playerW"] = scores["playerW"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Win")

    elif choice == 2 and compChoice == 1:
        scores["plays"] = scores["plays"] + 1
        scores["playerW"] = scores["playerW"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Win")

    elif choice == 3 and compChoice == 2:
        scores["plays"] = scores["plays"] + 1
        scores["playerW"] = scores["playerW"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Win")

    elif choice == 1 and compChoice == 2:
        scores["plays"] = scores["plays"] + 1
        scores["compW"] = scores["compW"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Lose")

    elif choice == 2 and compChoice == 3:
        scores["plays"] = scores["plays"] + 1
        scores["compW"] = scores["compW"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Lose")

    elif choice == 3 and compChoice == 1:
        scores["plays"] = scores["plays"] + 1
        scores["compW"] = scores["compW"] + 1
        print(f"Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']}")
        print(f"You: {options[choice]}, Computer: {options[compChoice]} Lose")


while play:
    choice = int(input("""
    \nPlease select an option:
    1) Rock
    2) Paper
    3) Scissors
    4) Quit the game
                       """))
    if choice == 1 or choice == 2 or choice == 3:
        game(choice)
    elif choice == 4:
        break
    else:
        print("Invalid option")
        continue

print("Thank you for playing")