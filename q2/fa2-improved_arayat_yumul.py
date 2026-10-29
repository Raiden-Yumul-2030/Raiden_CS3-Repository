class Patient:
  def __init__(self, name, bill_amount):
    self._name = name
    self._bill_amount = bill_amount
  def get_name(self):
    return self._name
  def set_name(self, name):
    self._name = name
  def get_bill_amount(self):
    return self._bill_amount
  def set_bill_amount(self, bill_amount):
    self._bill_amount = bill_amount
  def calculate_bill(self):
    print("Hospital Billing System\n---------------------")
    print("Patient name: ", self._name)
    print("Patient type: Regular Patient")
    print("Original bill: ₱", self._bill_amount)
    print("Final bill: ₱", self._bill_amount * 1)
    print("")

class SeniorPatient(Patient):
  def calculate_bill(self):
    print("Patient name: ", self._name)
    print("Patient type: Senior Citizen")
    print("Original bill: ₱", self._bill_amount)
    print("Final bill: ₱", self._bill_amount * 0.8)
    print("")
    
class PhilHealthPatient(Patient):
  def __init__(self, name, bill_amount):
     super().__init__(name, bill_amount)
  def calculate_bill(self):
    print("Patient name: ", self._name)
    print("Patient type: PhilHealth Member")
    print("Original bill: ₱", self._bill_amount)
    print("Final bill: ₱", self._bill_amount * 0.85)
    print("")

np1 = Patient("Juan Dela Cruz", 15000)
sp1 = SeniorPatient("Maria Santos", 15000)
php1 = PhilHealthPatient("Pedro Reyes", 15000)

np1.calculate_bill()
sp1.calculate_bill()
php1.calculate_bill()
