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
    def __init__(self, beakers):
        self.trayinventory = []
    def beaker_add(self):
        if len(self.trayinventory) < 5:
            self.trayinventory.append()
        else:
            print("Too many beakers on tray already!")
    def beakers(self):
        print(f"The beaker capacity of this tray is {len(self.trayinventory)}/5")

beaker = beaker("beaker")
beaker.inspect()
tray = tray("tray")
