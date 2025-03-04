import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox
import os
from PyQt6 import uic 
from bmi_design_source_code import Ui_MainWindow # importing design

class BMI(QMainWindow):
    def __init__(self):
        super().__init__() # inherits all from QMainWindow

        '''bmi_ui_path = os.path.join(os.path.dirname(__file__), "resources/bmi.ui")
        uic.loadUi(bmi_ui_path,self)''' # imorting file .ui 
        
        # 4 march update: I've decided to directly import the code file ".py" instead of ".ui" file

        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)
        self.setWindowTitle("BMI Calculator")

        self.ui.calt_bmi.clicked.connect(self.on_click) # here in parentheses we pass another instance method
        self.ui.selectUnitButton.clicked.connect(self.metric_selected)
        self.ui.actionClear.triggered.connect(self.in_menu_clear)
        self.ui.actionExit.triggered.connect(QApplication.quit)
        self.ui.actionHowUse.triggered.connect(self.show_help)
    
    def on_click(self):
        
        if self.ui.selectUnits.currentText() == "Metric":
            weight = float(self.ui.weight_input.text())
            height = float(self.ui.height_input.text())
            height/=100
            bmi_cal = weight/height**2
            self.ui.bmi_output.setText(f"{bmi_cal:.1f}")
            if bmi_cal < 18.5:
                self.ui.bmi_output.setStyleSheet("background-color: #f4c542; color: white; font: bold 14px; padding: 5px;")
            elif bmi_cal >= 18.5 and bmi_cal <25:
                self.ui.bmi_output.setStyleSheet("background-color: #4caf50; color: white; font: bold 14px; padding: 5px;")
            elif bmi_cal >=25 and bmi_cal <30:
                self.ui.bmi_output.setStyleSheet("background-color: #e57342; color: white; font: bold 14px; padding: 5px;")
            else:
                self.ui.bmi_output.setStyleSheet("background-color: #c62828; color: white; font: bold 14px; padding: 5px;")
        else:
            weight_imp = self.ui.weight_input.text()
            height_imp = self.ui.height_input.text()
            bmi_cal_imp = (int(weight_imp)*703)/(int(height_imp)**2)
            self.ui.bmi_output.setText(f"{bmi_cal_imp:.1f}")
            if bmi_cal_imp < 18.5:
                self.ui.bmi_output.setStyleSheet("background-color: #f4c542; color: white; font: bold 14px; padding: 5px;")
            elif bmi_cal_imp >= 18.5 and bmi_cal_imp <25:
                self.ui.bmi_output.setStyleSheet("background-color: #4caf50; color: white; font: bold 14px; padding: 5px;")
            elif bmi_cal_imp >=25 and bmi_cal_imp <30:
                self.ui.bmi_output.setStyleSheet("background-color: #e57342; color: white; font: bold 14px; padding: 5px;")
            else:
                self.ui.bmi_output.setStyleSheet("background-color: #c62828; color: white; font: bold 14px; padding: 5px;")

            
    def in_menu_clear(self):
        self.ui.weight_input.clear()
        self.ui.height_input.clear()
        self.ui.bmi_output.setText("")
        self.ui.bmi_output.setStyleSheet("")
    
    def metric_selected(self):
        if self.ui.selectUnits.currentText() == "Metric":
            self.ui.label_4.setText("kg")
            self.ui.label_5.setText("cm")
        else:
            self.ui.label_4.setText("lb")
            self.ui.label_5.setText("in")

    def show_help(self):
        QMessageBox.information(
            self, 
            "How to Use",  # Title
            "Welcome to the BMI Calculator!\n\n"
            "- Enter your weight and height.\n"
            "- Select the unit system (Metric or Imperial).\n"
            "- Click 'Calculate BMI' to get your result.\n"
            "- Use the 'Clear' option in the menu to reset inputs.\n"
            "- Exit the program from the 'Exit' option in the menu.\n\n"
            "Enjoy using the app!"
        )
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    name_app = BMI()
    name_app.show()
    sys.exit(app.exec())