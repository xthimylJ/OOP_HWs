from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size: float, battery_life: int):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    # instance method 
    def display_info(self): # overriding Device.display_info() method 
        return super().display_info() + f"Screen size of the smartphone: {self.screen_size}\n"\
                                      + f"Battery life of the smarphone: {self.battery_life}"
    
    # instance method 
    def make_call(self): # sm1.make_call() -> calling method
        print(f"Calling...")
    
    # instance method
    def install_app(self):
        print(f"Inatalling an app...")

    def __str__(self):
        return f"Smartphone: {self.name}"
    



# random note
"""We can call a static method in two ways:
        Class_name.staticmethod(),
        obj_of_the_class.staticmethod()"""