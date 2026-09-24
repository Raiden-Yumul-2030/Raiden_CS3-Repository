# DIDN'T FINISH
class Bank:
    name = ""
    def __init__(self, name):
        name = self.name
        self.__accounts = []

    def showAccounts(self):
        print("Showing Accounts")
        for i in range(len(self.__accounts)):
            print(self.__accounts[i])

    def openAccount(self):
        print("Ready to open an account")
        accName = input("Account name: ")
        accNum = int(input("Account number: "))
        accType = input("Account type (savings or checking): ").lower()
        broken = False
        while broken:
            if accType == "savings" or accType == "checking":
                broken = True
                continue
            else:
                print("Not a valid account type")
        print("Account Created")
        # account = print(self.)

    def closeAccount(self):
        print("Ready to close an account")
        accVer = int(input("Enter account number: "))
        broken = False
        while broken:
            if accNum == accVer:
                broken = True
                continue
            else:
                print("Incorrect PIN!")
        accountClose = input("Enter account number: ")

    def deposit(self):
        print("Ready to deposit an amount")
        accVer = int(input("Enter account number: "))
        broken = False
        while broken:
            if accNum == accVer:
                broken = True
                continue
            else:
                print("Incorrect PIN!")
        depositedAmount = float(input("Deposited amount: "))
        self.balance += depositedAmount
        print("Deposit successful")

    def addInterest(self):
        print("Adding interest to all savings accounts")
        for i in range(len(__accounts)):
            print("")
            
        


    def __del__():
        print(f"~ Thank you for banking with {self.name}")
        



class Account(Bank):
    def __init__(self, name, number, __balance = 0):
        self.name = name
        self.number = number

    def __str__(self, accName, accNum, accType):
        return f"{accName} [{accNum}] P {balance}"

    def __del__():
        pass
'''
    def getBalance(self):
        print("Ready to fetch account balance")
        print(f"{self.balance}")

    def deposit(self):
        print("Ready to deposit an amount")
        depositedAmount = float(input("Deposit to balance: "))
        self.balance += depositedAmount

    def withdraw(self):
        print("Ready to withdraw an amount")
        withdrawnAmount = float(input("Withdraw from balance: "))
        self.balance -= withdrawnAmount

class SavingsAccount:
    def __init__(self, interest = 0.05):
        pass

    def addInterest(self):
        addedInterest = float(input("Add to interest: "))
        self.interest += addedInterest
'''

mbtc = Bank("Metrobank")
mbtc.openAccount()
mbtc.openAccount()
mbtc.showAccounts()
mbtc.deposit()
mbtc.deposit()
mbtc.addInterest()
mbtc.closeAccount()

