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

bill = Bill(1000)
payment = Payment(1000)
bill.pay(payment)
