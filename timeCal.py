time1 = input("Enter time 1 (DD:HH:MM): ").split(":")
time2 = input("Enter time 2 (DD:HH:MM): ").split(":")

num1 = {"day": int(time1[0]), "hour": int(time1[1]), "minute": int(time1[2])}
num2 = {"day": int(time2[0]), "hour": int(time2[1]), "minute": int(time2[2])}

exit = False

while exit == False:
    option = int(input(
        """
        Time Calculator
        1- Add 2 times
        2- Find the difference between 2 times
        3- Convert to Hours
        4- Convert to Minutes
        5- Convert Minutes to Time
        6- Convert Hours to Time
        7- Convert Days to Time
        8- Exit
            Enter an option:
        """
    ))
    if option == 8:
        exit = True
    elif option == 1:
        sum = {"day": (num1["day"] + num2["day"]), "hour": (num1["hour"] + num2["hour"]), "minute": (num1["minute"] + num2["minute"])}
        print(f" The total time is {sum['day']}:{sum['hour']}:{sum['minute']} (days:hours:minute)")
    elif option == 2:
        sum = {"day": (num1["day"] - num2["day"]), "hour": (num1["hour"] - num2["hour"]), "minute": (num1["minute"] - num2["minute"])}
        print(f" The difference is {sum['day']}:{sum['hour']}:{sum['minute']} (days:hours:minute)")
    elif option == 3:
        hours = input("Enter time (DD:HH:MM): ").split(":")
        hours = {"day": int(hours[0]), "hour": int(hours[1]), "minute": int(hours[2])}
        print(f"The total is {float((hours['day']*24) + hours['hour'] + (hours['minute']/60))}")