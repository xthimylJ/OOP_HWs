from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton
import sys
from uis.cusMan_pageDes import Ui_Form
from cusManPage import CustomerManagementPage
from roomManPage import Room_Management_Page
from bookingsManPage import Bookings_Management_Page
from main_Page import Main_Page
from PyQt6 import QtCore, QtWidgets
import sys


# Main Window with stacked pages
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Booking System")
        #self.resize(800, 600)

        # Central widget
        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)

        # Page 1: Home screen
        self.home_page = Main_Page(self.stack)

        # Page 2: Customer management page
        self.customer_page = CustomerManagementPage(self.stack)

        # Page 3: Rooms management page
        self.rooms_page = Room_Management_Page(self.stack)

        # Page 4: Bookings management page
        self.bookigs_page = Bookings_Management_Page(self.stack)
        

        # Add both pages to the stack
        self.stack.addWidget(self.home_page)         # index 0
        self.stack.addWidget(self.customer_page)     # index 1
        self.stack.addWidget(self.rooms_page)        # index 2
        self.stack.addWidget(self.bookigs_page)      # index 3

        # Connect button to switch pages
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
