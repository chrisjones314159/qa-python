budget = 20

shakes = {1: {"name": "strawberry", "price": 5}, 2: {"name": "chocolate", "price": 6}, 3: {"name": "banana", "price": 7}}

while budget > 4:
    choice  = input(
        """\nWhat can I get for you?:
        1) Strawberry £5
        2) Chocolate £6
        3) Banana £7
        """).lower()
    
    if choice == "q":
        break

    elif int(choice) == 1:
        print(f"{shakes[int(choice)]['name']} Milkshake, thats £{shakes[int(choice)]['price']}.")
        budget = budget - shakes[int(choice)]['price']
        print(f"You have £ {budget} left")

    elif int(choice) == 2:
        if (budget - shakes[int(choice)]['price']) < 0:
            print(f"You dont have enough to buy this shake select again please. You have £{budget}")
            continue
        print(f"{shakes[int(choice)]['name']} Milkshake, thats £{shakes[int(choice)]['price']}.")
        budget = budget - shakes[int(choice)]['price']
        print(f"You have £ {budget} left")

    elif int(choice) == 3:
        if (budget - shakes[int(choice)]['price']) < 0:
            print(f"You dont have enough to buy this shake select again please. You have £{budget}")
            continue
        print(f"{shakes[int(choice)]['name']} Milkshake, thats £{shakes[int(choice)]['price']}.")
        budget = budget - shakes[int(choice)]['price']
        print(f"You have £ {budget} left")
    else:
        print("Invalid input, please try again.")
print(f"You have £{budget}, you don't have enough to buy anything, bye.")
    

