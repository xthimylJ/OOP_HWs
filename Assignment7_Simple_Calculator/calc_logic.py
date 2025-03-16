class Model:
    def __init__(self):
        self.expression:str = ""

    def add_to_expression(self, char:str):
        self.expression += str(char)
    
    def remove_last_character(self):
        self.expression += self.expression[-1]
    
    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        self.expression = str(eval(self.expression))
        return (self.expression)
    
    def get_expression(self):
        return (self.calculate())




        
