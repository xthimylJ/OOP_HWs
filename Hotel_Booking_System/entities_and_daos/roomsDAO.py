import sqlite3
from .entiites import Room

class Room_DAO:

    def __init__(self, dbfile = "C:\OOP_HWs\Hotel_Booking_System\hotelBookingSystem.sqlite"):
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
    
    

        