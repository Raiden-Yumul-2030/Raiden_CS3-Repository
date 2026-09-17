class Sauce:
     def __init__(self, sauce, taste):
          self.sauce = sauce
          self.taste = taste          
  
class Tusoktusok(Sauce):
     def tasting(self):
          print(f"You dip the Tusoktusok in {self.sauce}. It tastes {self.taste}")

Food = Tusoktusok("Vinegar", "Sour")
Food.tasting()