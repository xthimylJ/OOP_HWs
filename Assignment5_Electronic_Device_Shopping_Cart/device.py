class Device:
    def __init__(self, name:str, price:float, stock:int, warranty_period: int):
        
        # initializing instance attributes
        self.name = name 
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    # instance method: 
    def display_info(self): # device1.display_info() -> calling example
        return f"Name of the device: {self.name}\n" \
               f"Price of the device: {self.price}\n" \
               f"Number of units available: {self.stock}\n" \
               f"Warranty_period of the device: {self.warranty_period} year(s)\n"
    
    # instance method:
    def apply_discount(self, discount_percentage): # device1.apply_discount(10) -> calling example
        self.price = self.price - self.price*discount_percentage/100
    
    # instance method
    def is_available(self, amount): # device1.is_available(20) -> calling example
        if self.stock >= amount:
            return True
        elif self.stock < amount:
            return False

    # instance method    
    def reduce_stock(self, amount): # device1.reduce_stock(5) -> calling example
        self.stock -= amount

    def __str__(self):
        return self.display_info()



      