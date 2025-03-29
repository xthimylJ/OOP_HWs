import sqlite3
from entity_person import Employee


class EmployeeDAO: 

    """this class allows us to manipulate database through python scripts
 not directly through db managers like DBeaver"""
    

    def __init__(self, dbfile):
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

    '''def check_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        print("Tables in database:", tables)'''

    def get_by_id(self, id):
        sql = """
            SELECT * 
            FROM employee
            WHERE id = ?
        """ # sql is the string 
        self.cursor.execute(sql, (id, ))
        row = self.cursor.fetchone()

        if row:


            employee = Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
        else:
            employee = None

        return employee
    

    def insert(self, employee: Employee):
        #sal = employee.get_salary()
        script_sql = f"""
            INSERT INTO employee (id, name, position, salary, hire_date)
            VALUES (?, ?, ?, ?, ?)
        """ 
        self.cursor.execute(script_sql, (employee.id, employee.name, employee.position, employee.get_salary(), employee.hire_date))

        self.connection.commit()
        
    
    def get_all(self):
        sql_script = """
            SELECT * 
            FROM employee

        """
        self.cursor.execute(sql_script)
        rows = self.cursor.fetchall()
        
        employees = []
        for row in rows:
            employee = Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
            employees.append(employee)

        for i in employees:
            print(i) # if we try to just return employees list, it will print confusing memory addresses
    

    def update(self, employee:Employee):
        sql = """
            UPDATE employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        """ 
        self.cursor.execute(sql, (employee.name, employee.position, employee.get_salary(), employee.hire_date, employee.id))
        self.connection.commit()

    def delete(self, id):
        sql = """
            DELETE FROM employee
            WHERE id = ?

        """
        self.cursor.execute(sql, (id, ))
        self.connection.commit()
        


