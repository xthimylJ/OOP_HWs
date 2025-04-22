from PyQt6 import QtWidgets
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, QItemSelection
from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton
import sys
from uis.cusMan_pageDes import Ui_Form

from PyQt6 import QtCore, QtWidgets
import sys
from hotelBooking_model import Hotel_Booking_Model
from entities_and_daos.entiites import Customer
from entities_and_daos.customerDAO import CustomerDAO


class CustomerManagementPage(QtWidgets.QWidget):
    def __init__(self, stack_widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stack = stack_widget

        
        self.db = Hotel_Booking_Model()

        """self.tablemodel = CustomerTableModel(self.db.show_all())
        self.ui.customer_list.setModel(self.tablemodel)"""
        
        
        
        self.ui.refresh_button.clicked.connect(self.refresh_cus)
        self.ui.update_button.clicked.connect(self.update_cusinfo)
        self.ui.clear_field_button.clicked.connect(self.clear_fields)
        self.ui.delete_button.clicked.connect(self.delete_user)
        self.ui.back_tomain_menu.clicked.connect(self.back_to_main)

    def back_to_main(self):
        self.stack.setCurrentIndex(0)

    def delete_user(self):
        id = self.ui.id_show_label.text()
        self.db.delete_customer(id)
        self.clear_fields()

    def clear_fields(self):
        self.ui.id_show_label.clear()
        self.ui.full_name_input.clear()
        self.ui.email_input.clear()
        self.ui.phone_input.clear()

    def update_cusinfo(self):
        id = self.ui.id_show_label.text()
        name = self.ui.full_name_input.text()
        email = self.ui.email_input.text()
        phone = self.ui.phone_input.text()
        booking_id = self.ui.booking_id_lbl.text()

        cus = Customer(id, name, email, phone)
        self.db.update_customer_info(cus)
        self.db.sync_customer_name(booking_id)
    

    


    def refresh_cus(self):
        self.tablemodel = CustomerTableModel(self.db.show_all_customers())
        self.ui.customer_list.setModel(self.tablemodel)

        self.ui.customer_list.selectionModel().selectionChanged.connect(self.on_table_clicked)
        self.ui.customer_list.setColumnWidth(0, 40)
        self.ui.customer_list.setColumnWidth(4, 40)


    def on_table_clicked(self, selected: QItemSelection, deselected: QItemSelection):
        selected_indexes = selected.indexes()

        if selected_indexes:
            # Get the first selected index (assuming single selection)
            selected_index = selected_indexes[0]

            # Get the row of the selected item
            row = selected_index.row()

            # Access the Person object at the selected row
            selected_customer = self.tablemodel.cutomers[row]

            self.ui.full_name_input.setText(str(selected_customer[1]))
            self.ui.email_input.setText(str(selected_customer[2]))
            self.ui.phone_input.setText(str(selected_customer[3]))
            self.ui.id_show_label.setText(str(selected_customer[0]))
            self.ui.booking_id_lbl.setText(str(selected_customer[4]))
            self.ui.booking_date_lbl.setText(str(selected_customer[5]))

    

    






class CustomerTableModel(QAbstractTableModel):
    def __init__(self, customers=None):
        super().__init__()
        self.cutomers = customers or []
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.cutomers)
    
    def columnCount(self, parent=QModelIndex()):
        return 6
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self.cutomers[index.row()][index.column()])
        return None
    
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ['ID', 'Full Name', 'Email', 'Phone Number', "Booking_id", "Booking_date"]
            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
        return None
    
