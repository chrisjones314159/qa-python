# counter = 0

# while counter < 5:
#     name = input("Name: ")
#     print(f"{name} is great")
#     counter += 1

# # Lab 3
# # Task 1
# x = 1
# while x < 100:
#     if (x**2) > 2000:
#         break
#     print(x)
#     print(x**2)
#     x +=1

# # Task 2 
# num = int(input("Number: "))
# num2 = num
# while num > 1:
#     num2 = num2*(num-1)
#     num -=1
# print(num2)

# # Task 3
# initial = float(input("Initial: "))
# target = float(input("Target: "))
# Interest = float(input("Interest: "))

# while initial < target:
#     initial = initial+(initial*(Interest/100))
#     print(round(initial, 2))

# # Task 4
# attempt = 0
# while attempt < 3:
#     value = int(input("Enter a value between 1 and 100: "))
#     if 1 <= value <= 100:
#         print(f"Your value is {value}")
#         break
#     else:
#         attempt = attempt+1
#     print(attempt)
# print("Too many attempts, bye")

## task 5 count vowels
# word = input("Word: ").lower()
# vowels = 0
# x = 0
# while x < len(word):
#     if word[x] in "aeiou":
#         vowels = vowels + 1
#     x += 1
# print(vowels)

# # Exam Average
# valid = False

# while valid == False:
#     it = int(input("Enter a valid IT grade: "))
#     maths = int(input("Enter a valid Maths grade: "))
#     english = int(input("Enter a valid English grade: "))
#     if maths >= 0 and maths < 100 and it >= 0 and it < 100 and english >= 0 and english < 100:
#         valid = True
#     else:
#         valid = False

# average = (it+maths+english)/3
# print(f"Average = {average}")
# if average < 65:
#     print("Fail")
# else:
#     print("Pass")

# # Part 2 Task 1 Squares
# for num in range(100):
#     print(num)
#     print(num**2)
#     if num**2 > 2000:
#         break
#     else:
#         continue

# # Factorial
# num = int(input("Number: "))
# factorial = 1
# nums = []

# for x in range(num):
#     factorial = factorial*(x+1)
#     nums.append(x+1)

# nums = "x".join(str(e) for e in nums)
# print(f"{nums} = {factorial}")

# Lab 4 part 1

# ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,
#     68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25
#     ,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# print(len(ages))
# for a in ages:
#     print(a)

# for a in ages:
#     print(a+1)

# ages2 = []
# for a in ages:
#     if a >= 16 and a <= 65:
#         ages2.append(a)
#     else:
#         continue

# ages3 = ages2
# for b in ages2:
#     if b > 25:
#         ages3 = [value for value in ages3 if value != b]
# print(ages3)
# print(sorted(ages3))
