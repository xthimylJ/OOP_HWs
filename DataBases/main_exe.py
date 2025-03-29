from entity_person import Employee
from employeeDAO import EmployeeDAO

empl_db = EmployeeDAO("C:\OOP_HWs\DataBases\employee_db.sqlite")

ef = Employee(21, "Nazik", "Data Scientist", 250000, "2020-05-24")

try:
    empl_db.insert(ef)
    print("Nazik arrives to the company as Data Scientist")
except Exception as e:
    print("Employee already exists.")


print(empl_db.get_by_id(21))

print("Retrieving all employees...")
print(empl_db.get_all())

print("changing Nazik's position...")
ef.position = "Backend Developer"

empl_db.update(ef)
print("Nazik's position has been changed")
empl_db.delete(21)
print("Nazik's left the company.")


