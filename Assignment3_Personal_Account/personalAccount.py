from amount import Amount

class PesonalAccount:
    # for initialization of instances
    def __init__(self, account_number: int, account_holder: str):
        # instance attributes
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0
        self.__transactions = [] 
    

    def deposit(self, amount): # когда мы будем вызывать этот метод в мейн файле, 
                               # мы должны передать число
        
        deposit_amount_obj = Amount(amount, 'DEPOSIT')
        self.__transactions.append(deposit_amount_obj)
        self.__balance += amount

    def withdraw(self, amount):
        
        withdraw_amount_obj = Amount(amount, 'WITHDRAWAL')
        if self.__balance - amount <=0:
            print('Now enough money.')
        else:
            self.__transactions.append(withdraw_amount_obj)
            self.__balance -= amount
    
    def print_transaction_history(self):
        for i in self.__transactions:
            print('====================')
            print(i)

    def get_balance(self):
        print(f'Your current balance: {self.__balance}')
        return
    
    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self, desired_account_number):
        self.__account_number = desired_account_number

    def get_account_holder(self):
        return self.__account_holder
    
    def set_account_holder(self, desired_account_holder):
        self.__account_holder = desired_account_holder
    
    def __str__(self):
        return f'Account number: {self.__account_number}\n' \
               f'Account holder: {self.__account_holder}\n' \
               f'Balance: {self.__balance}\n' \
               f'Number of transactions: {len(self.__transactions)}'
    
    def __add__(self, amount):
        self.deposit(amount)
        return self
    
    def __sub__(self, amount):
        self.withdraw(amount)
        return self
        



    

    

    