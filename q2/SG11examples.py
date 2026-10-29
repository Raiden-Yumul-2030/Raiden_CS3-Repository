class Bill:
  def __init__(self, amount):
    self.amount = amount
  def pay(self, payment):
    self.amount -= payment.amount
    print("Payment made using ", payment.mode)
    print("Remaining bill: ", self.amount)

class Payment:
  mode = "Cash"
  def __init__(self, amount):
    self.amount = amount

class Ewallet(Payment):
  def __init__(self, name, amount):
    self.mode = name
    self.amount = amount

bill = Bill(1000)
payment = Payment(900)
bill.pay(payment)
gcash = Ewallet("GCash", 100)
bill.pay(gcash)
