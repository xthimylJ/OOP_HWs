
from entities_and_daos.customer_entity import Customer
from entities_and_daos.customerDAO import CustomerDAO
 

class Hotel_Booking_Model:
    def __init__(self):
        self.customerDaoObj = CustomerDAO()

    def add_customer_to_db(self, customer:Customer):
        
        self.customerDaoObj.insert(customer)

    def show_all_customers(self):
        customer_list = self.customerDaoObj.fetch_all()
        return customer_list
        
    
    









"""c1 = Customer(None, "nazik omurgazieva", "nazik@gmail.com", "895696")
some_cusdao = CustomerDAO()
model = Hotel_Booking_Model(customerDaoObj=some_cusdao)
model.add_customer_to_db(c1)"""