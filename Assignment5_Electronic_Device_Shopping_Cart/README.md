# Electronic Devices

## Device Class Documentation

### **Overview**

The `Device` class is designed to represent an electronic device in a store's inventory system. Each device has essential attributes like name, price, stock availability, and warranty period. This class offers functionality for displaying device information, applying discounts, checking availability, and updating stock after purchases.

---

### **Features**

- Store essential information about a device.
- Display device details in a user-friendly format.
- Apply discounts to the device's price.
- Check if a device is available in the desired quantity.
- Reduce stock after a purchase.

---

### **Usage Example**

```python
# Creating a new device instance
device1 = Device("iPhone 14", 999.99, 20, 1)

# Display device information
print(device1.display_info())

# Apply a discount of 10%
device1.apply_discount(10)
print(f"New discounted price: {device1.price}")

# Check if 5 units are available
if device1.is_available(5):
    print("Device is available for purchase.")
else:
    print("Not enough stock available.")

# Reduce stock after purchase
device1.reduce_stock(5)
print(f"Updated stock: {device1.stock}")
```



### **Attributes**

| Attribute        | Type    | Description                               |
|------------------|---------|-------------------------------------------|
| `name`           | `str`   | The name of the device                    |
| `price`          | `float` | The price of the device                   |
| `stock`          | `int`   | Number of units available in stock        |
| `warranty_period`| `int`   | Warranty period of the device in years    |

---

### **Methods**

| Method                       | Description                                                       |
|------------------------------|-------------------------------------------------------------------|
| `display_info()`             | Returns a formatted string displaying device details              |
| `apply_discount(percentage)` | Applies a discount to the device price based on given percentage |
| `is_available(amount)`       | Returns `True` if the requested amount is available, otherwise `False` |
| `reduce_stock(amount)`       | Reduces the available stock by the specified amount               |
| `__str__()`                  | Returns a string representation of the device using `display_info()` |

---

### **Example Output**

```
Name of the device: iPhone 14
Price of the device: 999.99
Number of units available: 20
Warranty_period of the device: 1 year(s)

New discounted price: 899.991
Device is available for purchase.
Updated stock: 15
```  


## Cart Class Documentation

### **Overview**

The `Cart` class is designed to manage the shopping cart system for an online store. It interacts with `Device` objects, allowing users to add or remove items, view cart contents, calculate the total price, and complete the checkout process. This class helps simulate a simple e-commerce cart system.

---

### **Features**

- Add devices to the cart with quantity checks.
- Remove devices or decrease the quantity of items in the cart.
- Display the list of items currently in the cart.
- Calculate and return the total price of all items.
- Handle checkout by reducing stock from the inventory and summarizing purchases.

---

### **Usage Example**

```python
from device import Device
from smartphone import Smartphone
from cart import Cart

# Create device instances
phone1 = Smartphone("iPhone 14", 999.99, 20, 1, 6.1, 20)
phone2 = Smartphone("Galaxy S21", 799.99, 15, 2, 6.2, 22)

# Initialize a cart
cart = Cart()

# Add devices to the cart
cart.add_device(phone1, 2)
cart.add_device(phone2, 1)

# Display the items in the cart
cart.print_items()

# Calculate and print total price
cart.get_total_price()
print(f"Total Price: ${cart.total_amount}")

# Checkout process
print(cart.checkout())
```



### **Attributes**

| Attribute      | Type    | Description                                           |
|----------------|---------|-------------------------------------------------------|
| `items`        | `list`  | List of tuples `(Device, amount)` in the cart         |
| `total_amount` | `float` | Total cost of all devices in the cart                 |

---

### **Methods**

| Method                         | Description                                                                      |
|-------------------------------|----------------------------------------------------------------------------------|
| `add_device(device, amount)`  | Adds a device to the cart if sufficient stock is available                        |
| `remove_device(device, amount)`| Removes a specific amount of a device from the cart; removes completely if zero   |
| `print_items()`               | Prints all items currently in the cart with their quantities                      |
| `get_total_price()`           | Calculates and updates the total price of all items in the cart                   |
| `checkout()`                  | Reduces stock for purchased items, displays a summary, and returns the total cost |

---

### **Example Output**

```
Name of the item  |            Amount
iPhone 14         |            2
Galaxy S21        |            1

Total Price: $2799.97

Name of the item   Amount  Price
iPhone 14             2      999.99
Galaxy S21            1      799.99
==============================
Total price: 2799.97
```

---


## Smartphone Class Documentation

### **Overview**

The `Smartphone` class is a subclass of the `Device` class, designed to represent smartphones with specific attributes like screen size and battery life. It inherits common device properties and methods while adding smartphone-specific functionalities like making calls and installing apps.

---

### **Features**

- Inherits common device attributes such as name, price, stock, and warranty period.
- Adds unique smartphone attributes: screen size and battery life.
- Overrides the `display_info` method to include smartphone-specific details.
- Provides methods for making calls and installing apps.

---

### **Usage Example**

```python
from device import Device
from smartphone import Smartphone

# Create a smartphone instance
phone = Smartphone("iPhone 14", 999.99, 20, 1, 6.1, 20)

# Display smartphone details
print(phone.display_info())

# Make a call
phone.make_call()

# Install an app
phone.install_app()
```




### **Attributes**

| Attribute       | Type    | Description                                   |
|-----------------|---------|-----------------------------------------------|
| `screen_size`   | `float` | Size of the smartphone screen in inches       |
| `battery_life`  | `int`   | Battery life of the smartphone in hours       |

---

### **Methods**

| Method                        | Description                                                              |
|------------------------------|--------------------------------------------------------------------------|
| `display_info()`             | Returns a string with detailed smartphone information                    |
| `make_call()`                | Simulates making a call                                                  |
| `install_app()`              | Simulates installing an app                                              |
| `__str__()`                  | Returns a string representation of the smartphone name                   |

---

### **Example Output**

```
Name of the device: iPhone 14
Price of the device: 999.99
Number of units available: 20
Warranty_period of the device: 1 year(s)
Screen size of the smartphone: 6.1
Battery life of the smartphone: 20

Calling...
Installing an app...
```

## Store Management Application

### Overview

This is a **menu-driven console application** designed to simulate an electronics store. The application allows users to browse devices, add items to their cart, view cart contents, and check the total amount before purchasing.

The system supports three categories of devices:

- **Smartphones**
- **Laptops**
- **Tablets**

Each device has specific attributes such as name, price, stock, warranty period, and additional features (like battery life for smartphones).

---

### Features

- Display a list of all available devices with detailed information.
- Add selected devices to a shopping cart with desired quantity.
- View cart contents and total purchase price.
- Real-time stock management upon adding items to the cart.
- Exit functionality to end the session.

---

### Classes Used

#### 1. **Device**

Base class containing common attributes and methods for all devices.

#### 2. **Smartphone, Laptop, Tablet**

Derived classes inheriting from `Device`, each with their own unique attributes.

#### 3. **Cart**

Handles adding, removing, and displaying items in the user's shopping cart.

---

### How to Use

1. **Run the Program:**

   - Launch the application in a Python environment.

2. **Menu Options:**

   - `#1 Show Devices`: Displays a list of all available devices with their details.
   - `#2 Show Cart`: Displays the items added to your cart and the total price.
   - `#3 Exit`: Exits the application.

3. **Adding Devices to Cart:**

   - After selecting `Show Devices`, input the number corresponding to the device you want to add.
   - Enter the quantity you wish to purchase.
   - If the stock is sufficient, the item will be added to your cart.

4. **Viewing Cart:**

   - Selecting `Show Cart` will display all items added along with their quantities and total cost.

5. **Exiting:**

   - Select `Exit` to end the session.

---

### Example Usage

```
--------Welcome to our store!--------
Please, choose an option:
#1 Show Devices
#2 Show Cart
#3 Exit

1

1. Name of the device: Galaxy S21
Price: $799.99
Stock: 25
Warranty: 2 years
Screen size: 6.2"
Battery life: 22 hours

Enter the number of the device to add to your cart (0 to cancel): 1
Enter amount in which you want to purchase the selected device: 2
Galaxy S21 has been added to your cart.
```










