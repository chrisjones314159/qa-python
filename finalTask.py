
class PasswordCheck():
    pass_ = None
    passwordStrength = 0
    commonPass = ["123456", "123456789","password" ,"12345","1234567", "1234567890" ,"letmein"
        ,"football" ,"guest" ,"a1b2c3" ,"Password1" ,"1234" ,"abc123", "12345678" ,"qwerty"
        ,"baseball", "unknown" ,"soccer"]

    enteredPasswords = []
    dictOfPasses = {}

    def __init__(self):
        self.manager()
    
    def __str__(self):
        return(self.pass_, self.commonPass, self.dictOfPasses, self.enteredPasswords)



    def manager(self):
        while True:
            self.passwordStrength = 0
            self.pass_ = input("""\n
Please enter your password: 
Enter 'exit' to end program.
Enter 'history' to see history.
: """)
            if self.pass_ == "exit":
                break

            elif self.pass_ == "history":
                self.passHistory()

            else:
                self.check(self.pass_)


    def check(self, pass_):
        if any(char.isupper() for char in pass_):
            self.passwordStrength += 1
        if any(char.islower() for char in pass_):
            self.passwordStrength += 1
        if any(char.isdigit() for char in pass_):
            self.passwordStrength += 1
        if self.pass_ not in self.commonPass:
            self.passwordStrength += 1
        if self.pass_ not in self.enteredPasswords:
            self.passwordStrength += 1
        self.enteredPasswords.append(self.pass_)
        self.assignValue(pass_)
        
    def assignValue(self, pass_):
        if self.passwordStrength <= 1:
            self.dictOfPasses.update({pass_: "Very Weak"})
        elif self.passwordStrength == 2:
            self.dictOfPasses.update({pass_: "Weak"})
        elif self.passwordStrength == 3:
            self.dictOfPasses.update({pass_: "Moderate"})
        elif self.passwordStrength == 4:
            self.dictOfPasses.update({pass_: "Strong"})
        elif self.passwordStrength == 5:
            self.dictOfPasses.update({pass_: "Very Strong"})

    def passHistory(self):
        for pas in self.enteredPasswords:
            print(f"Password: {pas}, Strength: {self.dictOfPasses[pas]}")


test1 = PasswordCheck()
print(test1.__str__())


