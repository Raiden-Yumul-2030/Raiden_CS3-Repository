class Person:
  _name = ""
  def __init__(self, name):
    self._name = name

class Student(Person):
  pass

class Employee(Person):
  pass

p1 = Person("Drax")
print(p1._name)
p2 = Person("Groot")
print(p2._name)
p3 = Person("Starlord")
print(p3._name)


class Father():
  pass

class Mother():
  pass

class You():
  pass
