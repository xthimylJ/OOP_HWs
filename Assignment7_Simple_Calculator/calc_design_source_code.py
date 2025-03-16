# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(452, 547)
        font = QtGui.QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        MainWindow.setStyleSheet("\n"
"  \n"
"   background-color: rgb(96, 96, 97); /* Dark gray background */\n"
"   padding: 20px;\n"
"   border-radius: 10px;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.int_output = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.int_output.setEnabled(False)
        self.int_output.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Digital")
        font.setPointSize(-1)
        self.int_output.setFont(font)
        self.int_output.setStyleSheet("width: 200px;\n"
"    height: 50px;\n"
"    background-color: rgb(214, 223, 207); /* Light greenish-gray */\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(95, 95, 97); /* Dark gray border */\n"
"    color: black;\n"
"    font-family: \'Digital\', sans-serif;\n"
"    font-size: 60px;\n"
"    text-align: right;\n"
"    padding: 5px 10px;\n"
"    display: flex;\n"
"    align-items: center;\n"
"    justify-content: flex-end;")
        self.int_output.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.int_output.setObjectName("int_output")
        self.verticalLayout.addWidget(self.int_output)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_plus.setEnabled(True)
        self.button_plus.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.button_plus.setFont(font)
        self.button_plus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 3, 2, 1, 1)
        self.int_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_9.setEnabled(True)
        self.int_9.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_9.setFont(font)
        self.int_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_9.setObjectName("int_9")
        self.gridLayout.addWidget(self.int_9, 0, 2, 1, 1)
        self.int_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_6.setEnabled(True)
        self.int_6.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_6.setFont(font)
        self.int_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_6.setObjectName("int_6")
        self.gridLayout.addWidget(self.int_6, 1, 2, 1, 1)
        self.int_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_1.setEnabled(True)
        self.int_1.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_1.setFont(font)
        self.int_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_1.setObjectName("int_1")
        self.gridLayout.addWidget(self.int_1, 2, 0, 1, 1)
        self.button_mul = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_mul.setEnabled(True)
        self.button_mul.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.button_mul.setFont(font)
        self.button_mul.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.button_mul.setObjectName("button_mul")
        self.gridLayout.addWidget(self.button_mul, 1, 3, 1, 1)
        self.int_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_0.setEnabled(True)
        self.int_0.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_0.setFont(font)
        self.int_0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_0.setObjectName("int_0")
        self.gridLayout.addWidget(self.int_0, 3, 0, 1, 1)
        self.int_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_3.setEnabled(True)
        self.int_3.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_3.setFont(font)
        self.int_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_3.setObjectName("int_3")
        self.gridLayout.addWidget(self.int_3, 2, 2, 1, 1)
        self.button_min = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_min.setEnabled(True)
        self.button_min.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.button_min.setFont(font)
        self.button_min.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.button_min.setObjectName("button_min")
        self.gridLayout.addWidget(self.button_min, 2, 3, 1, 1)
        self.int_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_5.setEnabled(True)
        self.int_5.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_5.setFont(font)
        self.int_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_5.setObjectName("int_5")
        self.gridLayout.addWidget(self.int_5, 1, 1, 1, 1)
        self.int_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_2.setEnabled(True)
        self.int_2.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_2.setFont(font)
        self.int_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_2.setObjectName("int_2")
        self.gridLayout.addWidget(self.int_2, 2, 1, 1, 1)
        self.button_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_clear.setEnabled(True)
        self.button_clear.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        self.button_clear.setFont(font)
        self.button_clear.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 3, 1, 1, 1)
        self.int_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_8.setEnabled(True)
        self.int_8.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_8.setFont(font)
        self.int_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_8.setObjectName("int_8")
        self.gridLayout.addWidget(self.int_8, 0, 1, 1, 1)
        self.button_devision = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_devision.setEnabled(True)
        self.button_devision.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.button_devision.setFont(font)
        self.button_devision.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.button_devision.setObjectName("button_devision")
        self.gridLayout.addWidget(self.button_devision, 0, 3, 1, 1)
        self.int_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_4.setEnabled(True)
        self.int_4.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_4.setFont(font)
        self.int_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_4.setObjectName("int_4")
        self.gridLayout.addWidget(self.int_4, 1, 0, 1, 1)
        self.button_equal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_equal.setEnabled(True)
        self.button_equal.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.button_equal.setFont(font)
        self.button_equal.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0); /* Light gray */\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.button_equal.setObjectName("button_equal")
        self.gridLayout.addWidget(self.button_equal, 3, 3, 1, 1)
        self.int_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.int_7.setEnabled(True)
        self.int_7.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.int_7.setFont(font)
        self.int_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 236, 237); /* Light gray */\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #555;\n"
"    border: 1px solid #aaa;\n"
"}\n"
"\n"
"\n"
"")
        self.int_7.setObjectName("int_7")
        self.gridLayout.addWidget(self.int_7, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 62))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.int_output.setText(_translate("MainWindow", "0"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.int_9.setText(_translate("MainWindow", "9"))
        self.int_6.setText(_translate("MainWindow", "6"))
        self.int_1.setText(_translate("MainWindow", "1"))
        self.button_mul.setText(_translate("MainWindow", "*"))
        self.int_0.setText(_translate("MainWindow", "0"))
        self.int_3.setText(_translate("MainWindow", "3"))
        self.button_min.setText(_translate("MainWindow", "-"))
        self.int_5.setText(_translate("MainWindow", "5"))
        self.int_2.setText(_translate("MainWindow", "2"))
        self.button_clear.setText(_translate("MainWindow", "c"))
        self.int_8.setText(_translate("MainWindow", "8"))
        self.button_devision.setText(_translate("MainWindow", "/"))
        self.int_4.setText(_translate("MainWindow", "4"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.int_7.setText(_translate("MainWindow", "7"))
