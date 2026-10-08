# this code was the solution to the summative assesment
class Bank:
  pass



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
    print("Account ",self.number," closed")



class SavingsAccount(Account):
  __interest = 0.05
  
  def addInterest(self):
    interestToAdd = super().getBalance() * self.__interest
    super().deposit(interestToAdd)
    
  def testSavings(self):
    print(super().getBalance())



acc1 = Account("JMRI", "1234")
acc1.deposit(500)
acc1.withdraw(100)
print(acc1)

acc2 = SavingsAccount("EG", "4567")
acc.deposit(400)
acc.withdraw(200)
acc2.addInterest()
print(acc2)
