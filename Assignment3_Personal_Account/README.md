# PersonalAccount Banking System

## Overview
This project implements a simple banking system using Python. It includes:
- `Amount` class to represent a transaction.
- `PersonalAccount` class to manage a user's bank account.

## Classes and Methods

### Amount Class
- **Attributes:**
  - `amount`: Transaction amount (float)
  - `timestamp`: Date and time of transaction (datetime)
  - `transaction_type`: Type of transaction (`'DEPOSIT'` or `'WITHDRAWAL'`)
- **Methods:**
  - `__init__(self, amount, transaction_type)`: Initializes transaction details.
  - `__str__(self)`: Returns a string representation of the transaction.

### PersonalAccount Class
- **Attributes:**
  - `account_number`: Unique account identifier (int)
  - `account_holder`: Name of the account holder (str)
  - `balance`: Current balance (float)
  - `transactions`: List of `Amount` objects
- **Methods:**
  - `__init__(self, account_number, account_holder)`: Initializes account details with zero balance.
  - `deposit(self, amount)`: Adds a deposit transaction.
  - `withdraw(self, amount)`: Withdraws funds ensuring sufficient balance.
  - `print_transaction_history(self)`: Displays transaction history.
  - `get_balance(self)`: Returns current balance.
  - `get_account_number(self)`, `set_account_number(self, account_number)`: Get/Set account number.
  - `get_account_holder(self)`, `set_account_holder(self, account_holder)`: Get/Set account holder's name.
  - `__str__(self)`: Returns a string representation of the account.
  - `__add__(self, amount)`: Shortcut for `deposit(amount)`.
  - `__sub__(self, amount)`: Shortcut for `withdraw(amount)`.



## Test Cases
- **Deposit 1000**: Account balance should increase.
- **Withdraw 500**: Account balance should decrease.
- **Withdraw 800 (Insufficient Balance)**: Should display an error.
- **Check balance after transactions**: Should display the correct final balance.



