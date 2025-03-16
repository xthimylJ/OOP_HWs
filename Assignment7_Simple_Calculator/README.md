# PyQt6 Calculator

A simple GUI-based calculator built using Python and PyQt6. This project implements basic arithmetic operations and a graphical user interface.

## Features

- **Basic Arithmetic Operations:** Addition, Subtraction, Multiplication, and Division.
- **Graphical Interface:** Built using PyQt6.
- **Error Handling:** Handles division by zero and invalid expressions.
- **Interactive Buttons:** Clickable buttons for numbers and operations.  
## Code Overview  
`Model` Class (Backend Logic)  
Located in `calc_logic.py`, this class handles expression management and calculations.  
#### Methods:  
- `add_to_expression(char: str)`: Adds a character to the current expression.
- `remove_last_character()`: Removes the last character (currently adds the last character instead).
- `clear_expression()`: Clears the expression.
- `calculate():` Evaluates the mathematical expression.
- `get_expression()`: Returns the calculated expression.  


`Calculator` Class (GUI Implementation)  
Located in `calculator.py`, this class integrates the GUI with logic.  
#### Key Components:
- Number & Operator Buttons: Clicking adds values to the expression.
- Equals Button: Evaluates the current expression.
- Clear Button: Resets the input.
#### Error Handling:
- SyntaxError: Displays "Error" for invalid expressions.
- ZeroDivisionError: Displays "Division by Zero!" when dividing by zero.  

## Usage  
Run the application using:
```sh
python calculator_app.py
```

## Screenshots  
![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/Subst_input.png)  

![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/subst_output.png)  

![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/multiplication_input.png)  

![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/mul_output.png)  

![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/wrong_format_of_input.png)  

![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/error_mes_screen.png)

![Simple Calculator Screenshots](https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment7_Simple_Calculator/screenshots/zero_div_handling.png)
