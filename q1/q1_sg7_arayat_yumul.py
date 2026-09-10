# BEAKERS!!
class glassware:
    def __init__(self, glassware_type):
        self.glassware_type = glassware_type
    def inspect(self):
            print(f"This glassware is called {self.glassware_type}")

class beaker(glassware):
    def __init__(self, glassware_type):
        super().__init__(glassware_type)
        self.glassware_type = "beaker"

class tray:
    def __init__(self):
        self.trayinventory = []
    def beaker_add(self):
        if len(self.trayinventory) < 5:
            self.trayinventory.append(beaker("beaker"))
        else:
            print("Too many beakers on tray already!")
    def beakercapacity(self):
        print(f"The beaker capacity of this tray is {len(self.trayinventory)}/5")

current_tray = tray()
beaker("beaker").inspect()
for i in range(5):
    current_tray.beaker_add()
    current_tray.beakercapacity()
del current_tray

input("Enter anything to end program: ")
