from device import Device
from cart_modified import Cart
from laptop import Laptop
from smartphone import Smartphone
from tablet import Tablet

# smartphones
phone1 = Smartphone("Galaxy S21", 799.99, 25, 2, 6.2, 22)
phone2 = Smartphone("iPhone 14", 999.99, 15, 1, 6.1, 20)
phone3 = Smartphone("Pixel 7", 599.99, 30, 2, 6.3, 24)
phone4 = Smartphone("OnePlus 11", 649.99, 20, 2, 6.7, 25)
phone5 = Smartphone("Xiaomi 13", 699.99, 18, 2, 6.36, 23)
phone6 = Smartphone("Sony Xperia 1 IV", 1099.99, 10, 1, 6.5, 21)

#laptops
laptop1 = Laptop("Dell XPS 13", 1199.99, 12, 2, 16, 3.5)
laptop2 = Laptop("MacBook Pro 16", 2499.99, 8, 1, 32, 3.2)
laptop3 = Laptop("HP Spectre x360", 1399.99, 10, 2, 16, 3.4)
laptop4 = Laptop("Lenovo ThinkPad X1 Carbon", 1599.99, 15, 3, 16, 3.6)
laptop5 = Laptop("Asus ROG Zephyrus G14", 1499.99, 5, 2, 32, 3.8)
laptop6 = Laptop("Acer Predator Helios 300", 1299.99, 7, 2, 16, 3.6)
laptop7 = Laptop("Microsoft Surface Laptop 5", 999.99, 20, 1, 8, 3.1)

# tablets
tablet1 = Tablet("iPad Pro 12.9", 1099.99, 10, 1, "2732x2048", 682)
tablet2 = Tablet("Samsung Galaxy Tab S8", 799.99, 12, 2, "2560x1600", 503)
tablet3 = Tablet("Microsoft Surface Pro 9", 999.99, 8, 1, "2880x1920", 879)
tablet4 = Tablet("Lenovo Tab P12 Pro", 649.99, 15, 2, "2560x1600", 565)
tablet5 = Tablet("Amazon Fire HD 10", 149.99, 25, 1, "1920x1200", 465)
tablet6 = Tablet("Huawei MatePad Pro", 749.99, 10, 2, "2560x1600", 460)
tablet7 = Tablet("Xiaomi Pad 5", 499.99, 20, 2, "2560x1600", 511)

cart = Cart()
# menu-driven app
all_devices = [
    phone1, phone2, phone3, phone4, phone5, phone6,
    laptop1, laptop2, laptop3, laptop4, laptop5, laptop6, laptop7,
    tablet1, tablet2, tablet3, tablet4, tablet5, tablet6, tablet7
]

# Menu-driven app
while True:
    print("\n--------Welcome to our store!--------")
    user_input = int(input("Please, choose an option: \n#1 Show Devices \n#2 Show Cart \n#3 Exit \n"))

    if user_input == 1:
        print("\n=======================")
        print("----- Available Devices -----")
        for index, item in enumerate(all_devices, 1):
            print(f"{index}. {item.display_info()}\n")

        # Prompt user to select a device to add to the cart
        
        selection = int(input("Enter the number of the device to add to your cart (0 to cancel): "))
        sel_amount = int(input("Enter amount in which you want to puchase the selected device: "))
        if 1 <= selection <= len(all_devices):
            selected_device = all_devices[selection - 1]
            cart.add_device(selected_device, sel_amount)  
            print()
            print(f"{selected_device.name} has been added to your cart.")
        elif selection == 0:
            print("Returning to the main menu.")
        else:
            print("Invalid selection. Please try again.")

    elif user_input == 2:
        print("\n=======================")
        print("----- Your Cart -----")
        cart.print_items()  
        cart.get_total_price()
        
        print("=======================")
        print(f"Total price: {cart.total_amount}")

    elif user_input == 3:
        print("Thank you for visiting our store! Goodbye!")
        break

    else:
        print("Invalid option. Please choose again.")