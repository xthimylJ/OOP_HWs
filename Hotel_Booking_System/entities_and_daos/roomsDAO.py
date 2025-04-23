import sqlite3
from .entiites import Room
import os

class Room_DAO:

    def __init__(self, dbfile = None):
        if dbfile is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dbfile = os.path.join(base_dir, "..", "hotelBookingSystem.sqlite")
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

    def fetch_all(self):
        sql = """
            SELECT * 
            FROM rooms
        
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall() 

        return rows
    
    

        