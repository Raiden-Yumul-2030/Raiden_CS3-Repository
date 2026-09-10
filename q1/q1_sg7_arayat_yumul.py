class glassware:
    def __init__(self, glassware_type):
        self.glassware_type = glassware_type
    def inspect(self):
        print(f"This glassware is called {self.glassware_type}")

class beaker(glassware):
    def __init__(self, beakers):
        super().__init__(glassware_type = "beaker")
        self.beakers = beakers
    def count(self):
        print(f"There is a {self.beakers} here")

beaker = beaker(glassware)
beaker.count()
beaker.inspect()
