import sqlite3
import os

from .entiites import Booking

class BookingsDAO:
    def __init__(self, dbfile = None):
        if dbfile is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dbfile = os.path.join(base_dir, "..", "hotelBookingSystem.sqlite")
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

    def get_from_bookings(self, selected_date):
        sql = """
            SELECT id, room_id, check_in, check_out, status
            FROM bookings
            WHERE DATE(:selected_date) BETWEEN check_in AND check_out

        """
        self.cursor.execute(sql, {"selected_date": selected_date})
        bookings = self.cursor.fetchall()
        return bookings
    
    def get_all(self):
        sql = """
            SELECT * 
            FROM bookings

        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
    
    def update_booking(self, booking: Booking):
        sql = """
            UPDATE bookings
            SET room_id = ?, check_in = ?, check_out = ?
            WHERE id = ?
        
        """
        self.cursor.execute(sql, (booking.room_id, booking.check_in, booking.check_out, booking.id))
        self.connection.commit()

    def cancel_booking(self, booking_id):
        sql = """
            UPDATE bookings 
            SET status = "Canceled"
            WHERE id = ?
        """
        self.cursor.execute(sql, (booking_id,))
        self.connection.commit()

