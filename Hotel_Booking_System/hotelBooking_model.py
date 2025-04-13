
from entities_and_daos.customer_entity import Customer
from entities_and_daos.customerDAO import CustomerDAO
 

class Hotel_Booking_Model:
    def __init__(self, customerDaoObj):
        self.customerDaoObj = customerDaoObj

    def add_customer_to_db(self, customer):
        self.customerDaoObj.insert(customer)

    def show_all(self):
        return self.customerDaoObj.fetch_all()
    
    









"""c1 = Customer(None, "nazik omurgazieva", "nazik@gmail.com", "895696")
some_cusdao = CustomerDAO()
model = Hotel_Booking_Model(customerDaoObj=some_cusdao)
model.add_customer_to_db(c1)"""