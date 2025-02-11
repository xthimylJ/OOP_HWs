from datetime import datetime

class Amount:
    def __init__(self, amount: float,  transaction_type):
        self.amount = amount 
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f'The amount of money transacted: {self.amount}\n' \
               f'When were the money transacted?: {self.timestamp}\n' \
               f'Transaction type: {self.transaction_type}'
    