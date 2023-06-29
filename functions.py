import statistics

# # Calculator

# def add(num1, num2 = 5):
#     return(f"{num1} + {num2} = {num1 + num2}")

# while True:
#     num1 = int(input("Number 1: "))
#     print(add(num1))


# # Lab 5 
# data= "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
# grades = list(map(int, data.split(",")))

# altGrades = [int(x) for x in data.split(",")]

# alt2Grades = []
# for grade in data.split(","):
#     alt2Grades.append(int(grade))

# print(alt2Grades)

# min = min(grades)
# max = max(grades)

# average = round(sum(grades)/len(grades), 2)

# mean = round(statistics.mean(grades), 2)
# median = statistics.median(grades)
# print("min is {}, max is {}, average is {}, mean is {}, median is {}".format(min, max, average, mean, median))


# # Lab 6
# def getIncomeTax(salary):
#     tax = 0
#     if salary <= 34500:
#         tax = (salary-11850)*0.2
#     elif salary <= 150000 and salary >=34501:
#         tax = (salary-11850)*0.2
#         tax = tax+(salary-34501)*0.4
#     elif salary > 150000 :
#         tax = (salary-11850)*0.2
#         tax = tax+(salary-34501)*0.4
#         tax = tax+(salary-150000)*0.45
#     return round(tax, 2)
# print(getIncomeTax(float(input("What is your salary: "))))


# # Password checker 
# def checker(passw):
#     passwords = ["admin123", "pass123"]
#     if passw in passwords:
#         print(f"Password: {passw} unsafe")
#     else:
#         print(f"Password: {passw} is safe")
# checker("admifsfef3")


# Calculator
def calculator(num1, num2):
    return(f"Sum: {num1}+{num2}={num1+num2}, minus {num1}-{num2}={num1-num2}, multiply {num1}*{num2}={num1*num2}")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first second: "))
print(calculator(num1, num2))