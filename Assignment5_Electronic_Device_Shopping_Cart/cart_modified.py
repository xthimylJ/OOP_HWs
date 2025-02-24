

from device import Device
from smartphone import Smartphone

class Cart:

    # instance attributes here! 
    def __init__(self):
        
        self.items = [] # list of tuples
        self.total_amount = 0 # The total price of all devices in the cart.


    
    # instance methods here!
    def add_device(self, device: Device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
        else:
            print(f"{device.name} is not available in required quantity")
        
         


    # instance method here!
    def remove_device(self, device: Device, amount):
        for i in range(len(self.items)):
            if self.items[i][0] == device:
                # Update the quantity (second element in the tuple)
                new_amount = self.items[i][1] - amount
                if new_amount <= 0:
                    del self.items[i]  # Remove the item if the amount goes to zero or negative
                else:
                    self.items[i] = (self.items[i][0], new_amount)  # Update the tuple with new quantity
                break
    
    # instance method
    def print_items(self):
        print("Name of the item  |            Amount")
        for pair in self.items:
            device = pair[0]
            amount = pair[1]
            print(f"{device}               {amount}")


    # instance method
    def get_total_price(self):
        self.total_amount = 0
        for i in range(len(self.items)):
            self.total_amount += self.items[i][0].price*self.items[i][1]
    
    # instnace method
    def checkout(self):
        
        print("Name of the item   Amount  Price")
        for pair in self.items:

            device = pair[0]
            amount = pair[1]
            print(f"{device.name}             {amount}      {device.price}")
            device.stock -= amount       
        print("==============================")
        self.get_total_price() # here we used instance method inside another instance method
        return f"Total price: {self.total_amount}"


      
"""
Smartphone 
""" 


# random note
"""
method(self) -> self in the parentheses means that we will work with class object data
method(cls) -> cls means we will work class data

"""