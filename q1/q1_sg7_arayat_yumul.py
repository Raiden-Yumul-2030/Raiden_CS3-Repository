class glassware:
    def __init__(self, glassware_type):
        self.glassware_type = glassware_type

class beaker(glassware):
    def __init__(self, beakers, glassware_type = "beaker"):
        super().__init__(glassware_type)
        self.beakers = []
    def inspect(self):
            print(f"This glassware is called {self.glassware_type}")
    def count(self):
        print(f"There are {self.beakers} here")

class tray(beaker):
    def __init__(self, beaker_amount):
        super().__init__(beakers)
        self.beaker_amount = len(self.beakers)

beaker = beaker("beaker")
beaker.inspect()
beaker.count()
