import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox
from calc_design_source_code import Ui_MainWindow 
from calc_logic import Model


class Calculator(QMainWindow):
    

    def __init__(self):
        super().__init__()
        self.calc = Ui_MainWindow()
        self.calc.setupUi(self)
        self.setWindowTitle("Calculator")
        self.ctrl = Model()
        
        
        self.calc.int_1.clicked.connect(lambda: self.int_click("1"))
        self.calc.int_0.clicked.connect(lambda: self.int_click("0"))
        self.calc.int_2.clicked.connect(lambda: self.int_click("2"))
        self.calc.int_3.clicked.connect(lambda: self.int_click("3"))
        self.calc.int_4.clicked.connect(lambda: self.int_click("4"))
        self.calc.int_5.clicked.connect(lambda: self.int_click("5"))
        self.calc.int_6.clicked.connect(lambda: self.int_click("6"))
        self.calc.int_7.clicked.connect(lambda: self.int_click("7"))
        self.calc.int_8.clicked.connect(lambda: self.int_click("8"))
        self.calc.int_9.clicked.connect(lambda: self.int_click("9"))
        self.calc.button_devision.clicked.connect(lambda: self.int_click("/"))
        self.calc.button_mul.clicked.connect(lambda: self.int_click("*"))
        self.calc.button_min.clicked.connect(lambda: self.int_click("-"))
        self.calc.button_plus.clicked.connect(lambda: self.int_click("+"))
        self.calc.button_equal.clicked.connect(self.clicked_equal)
        self.calc.button_clear.clicked.connect(self.clear_button)

    
    def int_click(self, input:str):
        self.ctrl.add_to_expression(input)
        self.calc.int_output.setText(str(self.ctrl.expression))
    
    def clicked_equal(self):
        try:
            output = self.ctrl.get_expression()
            self.calc.int_output.setText(output)
            #self.ctrl.clear_expression()
        except SyntaxError:
            self.calc.int_output.setText("Error")
        except ZeroDivisionError:
            self.calc.int_output.setText("Division by Zero!")

    
    def clear_button(self):
        self.ctrl.clear_expression()
        self.calc.int_output.setText("0")
        
    
        
    






    
        










if __name__ == '__main__':
    app = QApplication(sys.argv)
    name_app = Calculator()
    name_app.show()
    sys.exit(app.exec())
