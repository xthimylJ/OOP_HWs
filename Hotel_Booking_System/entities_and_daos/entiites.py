class Customer:
    def __init__(self, id, full_name, email, phone_num):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone_num = phone_num



class Booking:
    def __init__(self, id, customerFull_name, room_id, check_in, check_out,
                 booking_date, status="Active", total_price=0.0):
        self.id = id
        
        self.room_id = room_id
        self.customerFull_name = customerFull_name
        
        self.check_in = check_in
        self.check_out = check_out
        self.booking_date = booking_date
        self.status = status
        self.total_price = total_price
        


class Room:
    def __init__(self, id, room_num, room_type, price_per_night, status, check_in_date, check_out_date, booking_id):
        self.id = id
        self.booking_id = booking_id
        self.room_num = room_num
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.status = status
        
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date