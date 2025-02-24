from device import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        return super().display_info() + f"Screen screen resolution of the tablet: {self.screen_resolution}\n"\
                                      + f"Weight: {self.weight}"

    def __str__(self):
        return f'Tablet: {self.name}'


    def browse_internet(self):
        print("Browsing internet...")

    def use_touchscreen(self):
        print("Navigating the touchscreen...")

    
"""sm1 = Tablet("iPadPro", 1100, 20, 1, "2048 x 2732", 684)
print(sm1)"""