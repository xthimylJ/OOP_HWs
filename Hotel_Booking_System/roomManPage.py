from PyQt6 import QtWidgets
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, QItemSelection
from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton

from uis.room_des import Ui_Form
from hotelBooking_model import Hotel_Booking_Model


class Room_Management_Page(QWidget):

    def __init__(self, stack_widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stack = stack_widget
        self.db = Hotel_Booking_Model()

        self.ui.back_to_main.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.ui.view_rooms_btn.clicked.connect(self.view_rooms)
        self.ui.calendarWidget.selectionChanged.connect(self.update_label)
    
    def update_label(self):
        selected_date = self.ui.calendarWidget.selectedDate()  # QDate object
        date_str = selected_date.toString("dd-MM-yyyy")  # Format it however you like
        self.ui.selected_date_label.setText(date_str)

    def view_rooms(self):
        self.db.sync_rooms_with_bookings(self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd"))
        roomTable = RoomsTableModel(self.db.view_rooms())
        self.ui.rooms_view.setModel(roomTable)
        #self.ui.rooms_view.setColumnWidth(0, 40)
        #self.ui.rooms_view.setColumnWidth(1, 70)














class RoomsTableModel(QAbstractTableModel):
    def __init__(self, rooms=None):
        super().__init__()
        self.rooms = rooms or []
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.rooms)
    
    def columnCount(self, parent=QModelIndex()):
        return 8
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self.rooms[index.row()][index.column()]
            return str(value) if value is not None else ""

        return None
    
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            headers = ['ID', 'Room Num', 'Room type', 'Price per night', 'Status', 'booking_id', 'Check in date', 'Check out date', ""]
            if orientation == Qt.Orientation.Horizontal:
                return headers[section]
        return None
    
