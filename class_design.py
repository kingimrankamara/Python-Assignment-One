# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device Info: {self.brand} {self.model}"

# Derived class (Smartphone)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}"

    def device_info(self):
        base_info = super().device_info()
        return f"{base_info}, Storage: {self.storage}, Battery Life: {self.battery_life} hours"

# Creating instances of Smartphone
smartphone1 = Smartphone("Apple", "iPhone 14", "128GB", 20)
smartphone2 = Smartphone("Samsung", "Galaxy S21", "256GB", 22)

# Accessing methods and attributes
print(smartphone1.device_info())
print(smartphone1.make_call("123-456-7890"))
print(smartphone2.device_info())
print(smartphone2.make_call("987-654-3210"))
