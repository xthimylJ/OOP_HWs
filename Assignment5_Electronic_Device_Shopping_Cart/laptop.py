from device import Device
class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        return super().display_info() + f"Ram size of the laptop: {self.ram_size}\n"\
                                      + f"Processor_speed: {self.processor_speed}"

    def __str__(self):
        return f'Laptop: {self.name}'

    def run_program(self): 
        print("Running the program...")

    def use_keyboard(self):
        print("Using keyboard...")