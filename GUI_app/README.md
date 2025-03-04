# BMI Calculator

A simple **BMI (Body Mass Index) Calculator** built with **PyQt6**. This application allows users to calculate their BMI using either the **Metric** or **Imperial** system.

## Features
- **User Interface** built with PyQt6
- Supports **Metric (kg, cm)** and **Imperial (lbs, inches)** units
- **Color-coded BMI output** based on health categories
- **Help Menu** to guide users
- **Clear function** to reset input fields
- **Exit option** to close the application

## Installation
### Prerequisites
Ensure you have **Python 3.9** installed along with the required dependencies.

### Install Dependencies
```sh
pip install PyQt6
```

## How to Run the Application
1. Clone this repository or download the files.
2. Run the following command in the project directory:
```sh
python bmi_app.py
```

## Usage
1. Enter **weight** and **height** in the respective fields.
2. Select the **unit system** (Metric or Imperial) from the dropdown menu.
3. Click the **Calculate BMI** button to see your BMI value.
4. The output box will change color based on BMI classification:
   - **Yellow**: Underweight
   - **Green**: Normal
   - **Orange**: Overweight
   - **Red**: Obese
5. Use the **Help menu** (`Help -> How to Use`) for additional guidance.
6. Use the **Clear menu option** (`Edit -> Clear`) to reset the inputs.
7. Exit the application via the **Exit menu option** (`File -> Exit`).

## Code Overview
### **Main Class: `BMI(QMainWindow)`**
This class manages the main application window and handles user interactions.

### **Methods:**
- `on_click()`: Handles BMI calculation and updates the UI accordingly.
- `metric_selected()`: Updates unit labels based on the selected measurement system.
- `in_menu_clear()`: Clears all input fields and resets the output display.
- `show_help()`: Displays a help message using `QMessageBox`.  

### **Source code file: ``` bmi_design_source_code.py```**  
- This is just a ui design source code file ```.py```, which is imported in 
```sh
bmi_app.py
``` 
## Folders  
- ```resources``` folder contains ```bmi.ui``` file, which is crafted in pyqt6 designer.  
- ```screenshots_bmi``` folder contains usage sample screenshots 

## Screenshots  
- #### metric_units  
![BMI Calculator Screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/GUI_app/screenshots_bmi/metric_unit.png)  

- #### imperial_units  

![BMI Calculator Screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/GUI_app/screenshots_bmi/imperial_unit.png)  

- #### menu_file  
![BMI Calculator Screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/GUI_app/screenshots_bmi/menu_file.png)  

- #### menu_help  
![BMI Calculator Screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/GUI_app/screenshots_bmi/menu_help.png)






