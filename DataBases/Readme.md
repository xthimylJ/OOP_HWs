# Employee Database
## **Classes:**
### Entity class: **`Employee`**
- **Purpose:** maintains attributes of employees   
 
 ```python
    class Employee:
        def __init__(self, id, name, position, salary, hire_date):

            self.id = id
            self.name = name
            self.position = position
            self.__salary = salary
            self.hire_date = hire_date

```  
- **Method**:   
    - `get_salary()` : since salary is the private attribute
    - `set_salary(salary_amount: int)` : to modify the salary
    - `__str__()` : to represent an object as a string

### DAO Class: **`EmployeeDAO`**
- **Purpose:** is responsible for handling all interactions with the database  
- **Methods:**  
    - `__init__()` : for connection with the database
    - `get_by_id()` : retrieves an employee by her/his id
    - `insert()` : updates the database with new employee
    - `get_all()` : to retrieve all employees from the database
    - `update()` : to update the existing employee
    - `delete()` : to delete an employee from the database  

## **How to run and use the code:**  
- download "DataBase" folder from this repository 
- run the  
```sh
main_exe.py
```

## **Screenshots:**  
![Database screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/DataBases/Screenshots/employee_table.png)  


![Database screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/DataBases/Screenshots/employee_table_data.png)  


![Database screenshot](https://github.com/xthimylJ/OOP_HWs/blob/main/DataBases/Screenshots/Sample_output.png)

