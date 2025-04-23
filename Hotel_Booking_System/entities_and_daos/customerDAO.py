import sqlite3
from .entiites import Customer
import os

class CustomerDAO:
    def __init__(self, dbfile = None):
        if dbfile is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dbfile = os.path.join(base_dir, "..", "hotelBookingSystem.sqlite")
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

    def insert(self, customer: Customer):
        sql ="""
            INSERT INTO Customers (Full_name, Email, phone_number)
            VALUES (?, ?, ? )
        """
        self.cursor.execute(sql, (customer.full_name, customer.email, customer.phone_num))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def fetch_all(self):
        sql = """
            SELECT * 
            FROM Customers
        
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall() # "rows" variable is the list of tuples
        
        
        return rows
    
    def update(self, customer:Customer):
        sql = """
            UPDATE Customers
            SET Full_name = ?, Email = ?, phone_number = ?
            WHERE id = ?
        """ 
        self.cursor.execute(sql, (customer.full_name, customer.email, customer.phone_num, customer.id))
        self.connection.commit()
    
    def delete(self, id):
        sql = """
            DELETE FROM Customers
            WHERE id = ?

        """
        self.cursor.execute(sql, (id, ))
        self.connection.commit()

    def get_by_id(self, id):
        sql = """
            SELECT * 
            FROM Customers
            WHERE id = ?
        """ # sql is the string 
        self.cursor.execute(sql, (id, ))
        row = self.cursor.fetchone()
        return row 
