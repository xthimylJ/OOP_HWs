from PyQt6 import QtWidgets
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, QItemSelection
from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QMessageBox

from uis.bookingManPage_des import Ui_Form
from hotelBooking_model import Hotel_Booking_Model
from entities_and_daos.entiites import Booking
from entities_and_daos.entiites import Room


class Bookings_Management_Page(QWidget):
    def __init__(self, stack_widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = Hotel_Booking_Model()
        self.stack = stack_widget
        
        self.data = BookingsTableViewModel(self.db.view_bookings())
        self.ui.tableView.setModel(self.data)
        self.ui.tableView.setColumnWidth(0, 40)
        self.ui.tableView.setColumnWidth(1, 60)

        self.ui.back_to_main_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.ui.tableView.selectionModel().selectionChanged.connect(self.on_booking_clicked)
        self.ui.update_booking_btn.clicked.connect(self.update_booking)
        self.ui.cancel_booking_btn.clicked.connect(self.cancel_booking)
        self.ui.refresh_table_btn.clicked.connect(self.refresh_table)
        

    def refresh_table(self):
        self.data = BookingsTableViewModel(self.db.view_bookings())
        self.ui.tableView.setModel(self.data)
        self.ui.tableView.setColumnWidth(0, 40)
        self.ui.tableView.setColumnWidth(1, 60)
        self.ui.tableView.selectionModel().selectionChanged.connect(self.on_booking_clicked)


    def cancel_booking(self):
        booking_id = self.ui.booking_id_lbl.text()
        self.db.cancel_booking(booking_id)
        self.data = BookingsTableViewModel(self.db.view_bookings())
        self.ui.tableView.setModel(self.data)
        self.ui.tableView.setColumnWidth(0, 40)
        self.ui.tableView.setColumnWidth(1, 60)

        self.ui.tableView.selectionModel().selectionChanged.connect(self.on_booking_clicked)

    def update_booking(self):
        
        id = int(self.ui.booking_id_lbl.text())
        room_id = int(self.ui.room_id_change.text())
        check_in = self.ui.check_in_change.text()
        check_out = self.ui.check_out_change.text()
        booking = Booking(id, None, room_id, check_in, check_out, None, None, None)
        room = Room(room_id, None, None, None, None, None, None, None)
        available = self.db.is_room_available(room_id, check_in, check_out, id)
        if available:

            self.db.update_booking_info(booking)
            self.db.calculate_total_price(room, booking)

            self.data = BookingsTableViewModel(self.db.view_bookings())
            self.ui.tableView.setModel(self.data)
            self.ui.tableView.setColumnWidth(0, 40)
            self.ui.tableView.setColumnWidth(1, 60)

            self.ui.tableView.selectionModel().selectionChanged.connect(self.on_booking_clicked)
        else:
            QMessageBox.warning(
                self,  # parent widget (usually "self" inside a QMainWindow/QWidget)
                "Room Unavailable",
                "The selected room is already booked during these dates.\nPlease choose a different room or date range."
            )
            return


    def on_booking_clicked(self, selected: QItemSelection):
        selected_indexes = selected.indexes()

        if selected_indexes:
            row = selected_indexes[0].row()
            selected_booking = self.data.bookings[row]

            self.ui.booking_id_lbl.setText(str(selected_booking[0]))
            self.ui.room_id_change.setText(str(selected_booking[1]))
            self.ui.check_in_change.setText(str(selected_booking[3]))
            self.ui.check_out_change.setText(str(selected_booking[4]))
        









class BookingsTableViewModel(QAbstractTableModel):
    
    def __init__(self, bookings=None):
        super().__init__()
        self.bookings = bookings or []
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.bookings)
    
    def columnCount(self, parent=QModelIndex()):
        return 8
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self.bookings[index.row()][index.column()]
            return str(value) if value is not None else ""

        return None
    
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ['ID', 'Room ID', 'Customer Name', 'Check-in', 'Check-out', 'Booking Date', 'Total Price', "Status"]
            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
        return None