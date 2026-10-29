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





class Vehicle:
  color = ""
  def __init__(self, name, passengers):
    self.name = name
    self.passengers = passengers
  def move(self):
    print(f"The vehicle {self.name} is moving.")
    print(f"It has {self.passengers} passengers.")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  pass

class Toilet:
  def move(self):
    print("The vehicle toilet is moving... somehow.")
    print("It has 1 passenger.")

car = Car("car", 5)
boat = Boat("boat", 10)
plane = Vehicle("plane", 20)
toilet = Toilet()

vehicles = [car, boat, plane, toilet]
for v in vehicles:
  v.move()
