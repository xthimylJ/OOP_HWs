from PyQt6 import QtWidgets
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, QItemSelection
from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton

from uis.main_pageDes import Ui_Form


class Main_Page(QWidget):
    def __init__(self,stack_widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stack = stack_widget

        self.ui.manage_customers_btn.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.ui.manage_rooms_btn.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.ui.manage_bookings_btn.clicked.connect(lambda: self.stack.setCurrentIndex(3))
