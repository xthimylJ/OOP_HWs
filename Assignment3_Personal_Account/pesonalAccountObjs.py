from personalAccount import PesonalAccount
from amount import Amount


pa1 = PesonalAccount(230121019, "Omurgazieva Nazik")
pa1.deposit(256)
pa1.deposit(25)
pa1.withdraw(995)
pa1.withdraw(100)
#some_amount = Amount(256, 'WITHDRAWAL')
pa1 + 300
print(pa1.print_transaction_history())
print(pa1.get_balance())
print(pa1)
