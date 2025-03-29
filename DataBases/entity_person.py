class Employee:
    def __init__(self, id, name, position, salary, hire_date):

        self.id = id
        self.name = name
        self.position = position
        self.__salary = salary
        self.hire_date = hire_date

    
    def __str__(self):
        return f"Employee id: {self.id}, Name Surname: {self.name}"
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary_amount):
        self.__salary = salary_amount
        print(f"{self.name}'s salary is updated")

"""ef = Employee(1, "Nazik", "Data Scientist", 250000, "2020-05-24")
print(ef.get_salary())
ef.set_salary(300000)
print(ef.get_salary())
print(ef)"""