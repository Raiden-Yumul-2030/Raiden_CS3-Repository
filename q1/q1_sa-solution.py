# this code was the solution to the summative assesment
class Bank:
  name = ""
  __accounts = []
  
  def __init__(self, name):
    self.name = name
    print("Welcome to ", self.name)

  def openAccount(self):
    print("Ready to open an account")
    acc_name = input("Account name: ")
    acc_num = input("Account number: ")
    acc_type = input("Account type (savings or checking): ").lower()
    
    if acc_type == "savings":
      account = SavingsAccount(acc_name, acc_num)
    else:
      account = Account(acc_name, acc_num)
      
    self.__accounts.append(account)
    print("Account created")
    print(account)

  def showAccounts(self):
    print("Showing accounts")
    for a in self.__accounts:
      print(a)



class Account:
  name = ""
  number = ""
  __balance = 0
  
  def __init__(self, name, number):
    self.name = name
    self.number = number
    
  def deposit(self, amount):
    self.__balance += amount
    
  def withdraw(self, amount):
    if amount > self.__balance:
      print("Insufficient Funds")
    else:
      self.__balance -= amount
      
  def getBalance(self):
    return self.__balance
    
  def __str__(self):
    return self.name + " [" + self.number + "] P" + str(self.__balance)
    
  def __del__(self):
    print("Account ", self.number, " closed")



class SavingsAccount(Account):
  __interest = 0.05
  
  def addInterest(self):
    interestToAdd = super().getBalance() * self.__interest
    super().deposit(interestToAdd)


bank = Bank("Land Bank")
bank.openAccount()
bank.openAccount()
bank.showAccounts()
bank.deposit()
bank.deposit()
bank.addInterest()
bank.closeAccount()
