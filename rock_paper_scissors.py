import random
options = {1: "rock", 2: "paper", 3: "scissors"}
scores = {"playerW": 0, "compW": 0, "plays": 0, "draw": 0}

def output(choice, compChoice, outcome):
    return(f"""Games played: {scores['plays']}, Player Wins: {scores['playerW']}, Computer wins: {scores['compW']}, Draws: {scores['draw']} 
        You: {options[choice]}, Computer: {options[compChoice]} {outcome}""")

def game(choice):
    compChoice = random.randint(1, 3)
    outcome = None
    if choice == compChoice:
        scores["plays"] = scores["plays"] + 1
        scores["draw"] = scores["draw"] + 1
        outcome = "Draw"
        return(output(choice, compChoice, outcome))

    elif choice == 1 and compChoice == 3 or choice == 2 and compChoice == 1 or choice == 3 and compChoice == 2:
        scores["plays"] = scores["plays"] + 1
        scores["playerW"] = scores["playerW"] + 1
        outcome = "Win"
        return(output(choice, compChoice, outcome))

    elif choice == 1 and compChoice == 2 or choice == 2 and compChoice == 3 or choice == 3 and compChoice == 1:
        scores["plays"] = scores["plays"] + 1
        scores["compW"] = scores["compW"] + 1
        outcome = "Lose"
        return(output(choice, compChoice, outcome))

while True:
    choice = int(input("""
    \nPlease select an option:
    1) Rock
    2) Paper
    3) Scissors
    4) Quit the game
                       """))
    if choice == 1 or choice == 2 or choice == 3:
        print(game(choice))
    elif choice == 4:
        break
    else:
        print("Invalid option")
        continue

print("Thank you for playing")