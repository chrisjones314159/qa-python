import math
# mark = int(input("Grade: "))

# if mark > 85:
#     print("Distinction")
# elif mark > 65:
#     print("Pass")
# else:
#     print("Fail")

# weight = float(input("Weight: "))
# unit = input("Unit (kg or lbs): ").lower()

# if unit == "kg":
#     print(weight*2.205)
# else:
#     print(weight/2.205)

# # Chap 2 lab part 1
# age = 15
# if age >= 18:
#     print("Category A")
# elif age >=16:
#     print("Category B")
# else:
#     print("Category C")

# # Part 2
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))

# operation = input("Which operation (+ * / -): ")

# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# else:
#     print(num1 / num2)

# # TASK 2
# grade = int(input("Grade: "))

# if grade > 100 or grade < 0:
#     print("Unsuitable value")
# elif grade >= 71:
#     print("Distinction")
# elif grade >= 61:
#     print("Merit")
# elif grade >= 50:
#     print("Pass")
# elif grade < 50:
#     print("Fail")
# else:
#     print("Something bad happened")

# # Task 3
# grade = int(input("Grade: "))
# level = int(input("Level (1 or 2): "))

# if grade > 100 or grade < 0:
#     print("Grade value is not suitable")
# elif level == 1:
#     if grade >= 71:
#         print("Distinction")
#     elif grade >= 61:
#         print("Merit")
#     elif grade >= 50:
#         print("Pass")
#     elif grade < 50:
#         print("Fail")
#     else:
#         print("Something bad happened")
# elif level == 2:
#     if grade >= 66:
#         print("Distinction")
#     elif grade >= 51:
#         print("Merit")
#     elif grade >= 40:
#         print("Pass")
#     elif grade < 40:
#         print("Fail")
#     else:
#         print("Something bad happened")
# else:
#     print("Level Value not suitable")


# # Task 4
# choice = int(input("""
# Pythagoras' Calculator
# 1. Find the length of A given B and C
# 2. Find the length of B given A and C
# 3. Find the length of C given A and B
# """))

# if choice < 1 or choice > 3:
#     print("Invalid choice")
# elif choice == 1:
#     c = int(input("C: "))
#     b = int(input("B: "))
#     print(f"A = {math.sqrt(c**2 + b**2)}")
# elif choice == 2:
#     a = int(input("A: "))
#     c = int(input("C: "))
#     print(f"B = {math.sqrt(c**2 + a**2)}")
# elif choice == 3:
#     a = int(input("A: "))
#     b = int(input("B: "))
#     print(f"C = {math.sqrt(a**2 + b**2)}")
# else:
#     print("Something went wrong")


# extra-if task
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

max = 0

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

if (max % 2) != 0 and (max % 3) == 0:
    print("Odd, multiple of 3")
elif (max % 2) != 0:
    print("Odd")
else:
    print("Even")