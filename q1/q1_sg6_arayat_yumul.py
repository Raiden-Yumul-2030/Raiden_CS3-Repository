class Lab:
    def __init__(self, room_number):
        self.room_number = room_number
        
class Technician:
    def __init__(self, name):
        self.name = name
    def assign_lab(self, lab_obj):
        print(self.assigned_lab.room_number)

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
