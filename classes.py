class Student:
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_
    
    def test_scores(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3

    def setClass(self, class_):
        self.class_ = class_

    def getClass(self):
        return self.class_
    
    def getName(self):
        return self.name

student1 = Student("Sally", 13, "maths")
student2 = Student("Pete", 14, "it")

print(student1.age)
student1.setClass("English")
print(f"{student1.getName()} is in {student1.getClass()} class.")
print(student2.name)
print(student1.test_scores(5, 7, 6))

class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def noise(self):
        return "Noise"

class Owl(Bird):
    def __init__(self, name, age, nocturnal):
        super().__init__(name, age)
        self.nocturnal = nocturnal

class Dodo(Bird):
    def __init__(self, name, age, extinct):
        super().__init__(name, age)
        self.extinct = extinct

dodo1 = Dodo("Dave", 5, True)
owl1 = Owl("Oswald", 35, True)

print(owl1.nocturnal)
print(owl1.name)
print(owl1.age)

print(dodo1.extinct)
print(dodo1.name)
print(dodo1.age)
print(dodo1.noise())

# Bank Account
class Bank_Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, add):
        self.balance += add
    
    def withdraw(self, away):
        self.balance -= away

account = Bank_Account(1234, 50)

print(account.getBalance())
account.withdraw(20)
print(account.getBalance())
account.deposit(200)
print(account.getBalance())

# Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year
    
car = Car("Ford", "Focus", 2015)

print(car.getMake())
print(car.getModel())
print(car.getYear())

car.setMake("Kia")
car.setModel("Picanto")
car.setYear(2020)

print(car.getMake())
print(car.getModel())
print(car.getYear())

# Products
products = []

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return(self.name, self.price, self.quantity)

    def value(self):
        return self.price * self.quantity

    def addToProducts(self):
        products.append(self)

    def removeFromProducts(self):
        products.remove(self)


soap = Product("Dove", 2.99, 7)
pens = Product("Bic", 1, 10)

soap.addToProducts()
pens.addToProducts()

print(products[0].value())
print(products[1].value())

x = 0
while x < len(products):
    print(products[x].__str__())
    x += 1

pens.removeFromProducts()

x = 0
while x < len(products):
    print(f"New list, after pens have been removed: {products[x].__str__()}")
    x += 1