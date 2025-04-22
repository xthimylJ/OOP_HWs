import sqlite3
from entities_and_daos.entiites import Customer
from entities_and_daos.customerDAO import CustomerDAO
from entities_and_daos.entiites import Room
from entities_and_daos.roomsDAO import Room_DAO
from entities_and_daos.entiites import Booking
from entities_and_daos.bookingsDAO import BookingsDAO
 

class Hotel_Booking_Model:
    def __init__(self):
        self.connection = sqlite3.connect("C:\OOP_HWs\Hotel_Booking_System\hotelBookingSystem.sqlite")
        self.cursor = self.connection.cursor()
        self.__customerDaoObj = CustomerDAO()
        self.__roomsDaoObj = Room_DAO()
        self.__bookingDaoObj = BookingsDAO()


    def add_customer_to_db(self, customer:Customer):
        
        return self.__customerDaoObj.insert(customer)


    def show_all_customers(self):
        customer_list = self.__customerDaoObj.fetch_all()
        return customer_list
    
    def update_customer_info(self, customer: Customer):
        self.__customerDaoObj.update(customer)

    def delete_customer(self, id):
        
        self.__customerDaoObj.delete(id)
    
    def view_rooms(self):
        rooms = self.__roomsDaoObj.fetch_all()
        return rooms
    
    def view_bookings(self):
        return self.__bookingDaoObj.get_all()
    
    def sync_rooms_with_bookings(self, selected_date):
        bookings = self.__bookingDaoObj.get_from_bookings(selected_date)
        
        booked_room_ids = []

        for booking in bookings: 
            booking_id, room_id, check_in, check_out, booking_status = booking
            booked_room_ids.append(room_id)

            if booking_status in ['Confirmed', 'Paid']:
                room_status = 'Booked'
            else:
                room_status = 'Available'

        # Step 3: Update corresponding room
            sql_update_room = """
                UPDATE rooms
                SET booking_id = :booking_id,
                    check_in_date = :check_in,
                    check_out_date = :check_out,
                    status = :room_status
                WHERE id = :room_id
            """
            self.cursor.execute(sql_update_room, {
                "booking_id": booking_id,
                "check_in": check_in,
                "check_out": check_out,
                "room_status": room_status,
                "room_id": room_id
            })

    # Step 4: For all rooms NOT booked on selected date → reset fields
        sql_clear_unbooked = """
            UPDATE rooms
            SET booking_id = NULL,
                check_in_date = NULL,
                check_out_date = NULL,
                status = 'Available'
            WHERE id NOT IN ({})
        """.format(",".join("?" * len(booked_room_ids)) if booked_room_ids else "SELECT id FROM rooms")
    
        if booked_room_ids:
            self.cursor.execute(sql_clear_unbooked, booked_room_ids)
        else:
        # No rooms booked? Reset all
            self.cursor.execute("UPDATE rooms SET booking_id = NULL, check_in_date = NULL, check_out_date = NULL, status = 'Available'")

        self.connection.commit()

    def update_booking_info(self, booking: Booking):
        self.__bookingDaoObj.update_booking(booking)

    def calculate_total_price(self, room: Room, booking: Booking):
        sql = """
            SELECT price_per_night
            FROM rooms
            WHERE id = ?
        """
        self.__roomsDaoObj.cursor.execute(sql, (room.id,))
        price_per_night = self.__roomsDaoObj.cursor.fetchone()[0]

        sql2 = """
            SELECT julianday(check_out) - julianday(check_in) AS diff
            FROM bookings
            WHERE id = ? AND room_id = ?;

        """
        self.__bookingDaoObj.cursor.execute(sql2, (booking.id, booking.room_id))
        staying_days = self.__bookingDaoObj.cursor.fetchone()[0]

        total_price = price_per_night * staying_days

        sql3 = """
            UPDATE bookings
            SET total_price = ?
            WHERE id = ? AND room_id = ?
        """
        self.__bookingDaoObj.cursor.execute(sql3, (total_price, booking.id, booking.room_id))
        self.__bookingDaoObj.connection.commit()

    def is_room_available(self, room_id: int, new_check_in: str, new_check_out: str, booking_id: int = None) -> bool:
        sql = """
            SELECT 1 FROM bookings
            WHERE room_id = ?
            AND (
                (date(check_in) < date(?) AND date(check_out) > date(?))  -- overlap in middle
                OR (date(check_in) >= date(?) AND date(check_in) < date(?)) -- starts during
                OR (date(check_out) > date(?) AND date(check_out) <= date(?)) -- ends during
            )
        """
        params = [room_id, new_check_out, new_check_in, new_check_in, new_check_out, new_check_in, new_check_out]

        
        if booking_id:
            sql += " AND id != ?"
            params.append(booking_id)

        self.__bookingDaoObj.cursor.execute(sql, tuple(params))
        result = self.__bookingDaoObj.cursor.fetchone()
        return result is None
    
    def cancel_booking(self, booking_id):
        self.__bookingDaoObj.cancel_booking(booking_id)
    
    def sync_customer_name(self, booking_id):
        sql = """
            SELECT Full_name
            FROM Customers
            WHERE booking_id = ?

        """
        self.__customerDaoObj.cursor.execute(sql, (booking_id,))
        name = self.__customerDaoObj.cursor.fetchone()[0]

        sql1 = """
            UPDATE bookings
            SET customer_full_name = ?
            WHERE id = ?

        """
        self.__bookingDaoObj.cursor.execute(sql1, (name, booking_id))
        self.__bookingDaoObj.connection.commit()

        



        
    
    










