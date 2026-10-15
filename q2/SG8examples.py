class AStudent:
  def __init__(self, name, age):
    self.__name = name
    self.__age = 0
    self.set_age(age)
    
#setter and gtetter methods for name
def set_name(self, name):
  self.__name = name:
def get_name(self):
  return "Hello my name is " + self.__name

#setter and getter methods for age
def set_age(self, age):
  if age > 0:
    self.__age = age
def get_age(self):
  return self.__age

As = AStudent("******", 14)
As.set_age(-15)
print(As.get_age())
print(As.get_name())



class BStudent:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  # special getter by treating like a property
  # even though it's a function
  @property
  def name(self):
    return "Hello my name is " + self.__name
  @property
  def age(self):
    return "I am " + str(self.__age) + " years old"
  @name.setter
  def name(self, value):
    self.__name = value
  @age.setter
  def age(self, value):
    if value > 0:
      self.__age = value

Bs = BStudent("JM", 30)
Bs.name = "Sir Bern"
Bs.age = 31
print(Bs.name + Bs.age)
