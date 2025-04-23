import unittest
from unittest.mock import MagicMock, patch
from hotelBooking_model import Hotel_Booking_Model
from entities_and_daos.entiites import Customer, Room, Booking


class TestHotelBookingModel(unittest.TestCase):

    def setUp(self):
        self.model = Hotel_Booking_Model()
        self.model._Hotel_Booking_Model__customerDaoObj = MagicMock()
        self.model._Hotel_Booking_Model__roomsDaoObj = MagicMock()
        self.model._Hotel_Booking_Model__bookingDaoObj = MagicMock()
        self.model.connection = MagicMock()
        self.model.cursor = MagicMock()

    def test_add_customer_to_db(self):
        customer = Customer()
        self.model._Hotel_Booking_Model__customerDaoObj.insert.return_value = True
        result = self.model.add_customer_to_db(customer)
        self.model._Hotel_Booking_Model__customerDaoObj.insert.assert_called_with(customer)
        self.assertTrue(result)

    def test_show_all_customers(self):
        self.model._Hotel_Booking_Model__customerDaoObj.fetch_all.return_value = ['cust1', 'cust2']
        result = self.model.show_all_customers()
        self.assertEqual(result, ['cust1', 'cust2'])

    def test_update_customer_info(self):
        customer = Customer()
        self.model.update_customer_info(customer)
        self.model._Hotel_Booking_Model__customerDaoObj.update.assert_called_with(customer)

    def test_delete_customer(self):
        self.model.delete_customer(1)
        self.model._Hotel_Booking_Model__customerDaoObj.delete.assert_called_with(1)

    def test_view_rooms(self):
        self.model._Hotel_Booking_Model__roomsDaoObj.fetch_all.return_value = ['room1']
        result = self.model.view_rooms()
        self.assertEqual(result, ['room1'])

    def test_view_bookings(self):
        self.model._Hotel_Booking_Model__bookingDaoObj.get_all.return_value = ['booking1']
        result = self.model.view_bookings()
        self.assertEqual(result, ['booking1'])

    def test_is_room_available_true(self):
        self.model._Hotel_Booking_Model__bookingDaoObj.cursor.fetchone.return_value = None
        available = self.model.is_room_available(1, '2025-04-25', '2025-04-30')
        self.assertTrue(available)

    def test_is_room_available_false(self):
        self.model._Hotel_Booking_Model__bookingDaoObj.cursor.fetchone.return_value = (1,)
        available = self.model.is_room_available(1, '2025-04-25', '2025-04-30')
        self.assertFalse(available)

    def test_cancel_booking(self):
        self.model.cancel_booking(123)
        self.model._Hotel_Booking_Model__bookingDaoObj.cancel_booking.assert_called_with(123)

    def test_sync_customer_name(self):
        self.model._Hotel_Booking_Model__customerDaoObj.cursor.fetchone.return_value = ["John Doe"]
        self.model.sync_customer_name(101)
        self.model._Hotel_Booking_Model__bookingDaoObj.cursor.execute.assert_called_with(
            """
            UPDATE bookings
            SET customer_full_name = ?
            WHERE id = ?
            """, ("John Doe", 101)
        )


if __name__ == '__main__':
    unittest.main() 
