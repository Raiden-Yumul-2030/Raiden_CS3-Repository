#burger

from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2"
    def __str__(self):
        return "[pH Sensor] Reading: " + self.get_reading() + " pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5"
    def __str__(self):
        return "[Temperature Sensor] Reading: " + self.get_reading() + "°C"

pHSensor = PHSensor()
tempSensor = TempSensor()
print("--- Lab Inventory System ---")
print(pHSensor)
print(tempSensor)
print("----------------------------")
