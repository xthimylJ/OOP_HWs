# Form implementation generated from reading ui file 'bmi.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        MainWindow.setMinimumSize(QtCore.QSize(350, 350))
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weight = QtWidgets.QLabel(parent=self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(50, 40, 49, 21))
        self.weight.setStyleSheet("font: 14px;")
        self.weight.setObjectName("weight")
        self.height = QtWidgets.QLabel(parent=self.centralwidget)
        self.height.setGeometry(QtCore.QRect(50, 80, 49, 21))
        self.height.setStyleSheet("font: 14px;")
        self.height.setObjectName("height")
        self.weight_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.weight_input.setGeometry(QtCore.QRect(110, 40, 113, 21))
        self.weight_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.weight_input.setObjectName("weight_input")
        self.height_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.height_input.setGeometry(QtCore.QRect(110, 80, 113, 21))
        self.height_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.height_input.setObjectName("height_input")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 49, 21))
        self.label_4.setStyleSheet("font: 14px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 80, 49, 21))
        self.label_5.setStyleSheet("font: 14px;")
        self.label_5.setObjectName("label_5")
        self.calt_bmi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calt_bmi.setGeometry(QtCore.QRect(60, 120, 131, 31))
        self.calt_bmi.setStyleSheet("font: 14px;")
        self.calt_bmi.setObjectName("calt_bmi")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 170, 61, 16))
        self.label.setStyleSheet("font: 14px;")
        self.label.setObjectName("label")
        self.bmi_output = QtWidgets.QLabel(parent=self.centralwidget)
        self.bmi_output.setGeometry(QtCore.QRect(120, 170, 71, 21))
        self.bmi_output.setStyleSheet("")
        self.bmi_output.setText("")
        self.bmi_output.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bmi_output.setObjectName("bmi_output")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 230, 331, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setStyleSheet("background-color: #f4c542; \n"
"color: white;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("background-color: #4caf50; \n"
"color: white;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"border-radius: 5px;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setStyleSheet("background-color: #e57342; \n"
"color: white;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_7.setStyleSheet("background-color: #c62828; \n"
"color: white;\n"
"font: bold 14px;\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 10, 49, 16))
        self.label_8.setStyleSheet("font: 14px")
        self.label_8.setObjectName("label_8")
        self.selectUnits = QtWidgets.QComboBox(parent=self.centralwidget)
        self.selectUnits.setGeometry(QtCore.QRect(110, 10, 111, 22))
        self.selectUnits.setEditable(False)

        # adding items to combobox

        self.selectUnits.addItem("Metric")
        self.selectUnits.addItem("Imperial")
        self.selectUnits.setCurrentText("")
        self.selectUnits.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.selectUnits.setMinimumContentsLength(2)
        self.selectUnits.setObjectName("selectUnits")
        self.selectUnitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.selectUnitButton.setGeometry(QtCore.QRect(240, 10, 75, 24))
        self.selectUnitButton.setObjectName("selectUnitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar) 
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionClear = QtGui.QAction(parent=MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionHowUse = QtGui.QAction(parent=MainWindow)
        self.actionHowUse.setObjectName("actionHowUse")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionClear)
        self.menuHelp.addAction(self.actionHowUse)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.selectUnits.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.weight.setText(_translate("MainWindow", "Weight"))
        self.height.setText(_translate("MainWindow", "Height"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.calt_bmi.setText(_translate("MainWindow", "Calculate BMI"))
        self.label.setText(_translate("MainWindow", "Your BMI:"))
        self.label_2.setText(_translate("MainWindow", "Underweigt < 18.5"))
        self.label_3.setText(_translate("MainWindow", "Normal 18.5 - 25"))
        self.label_6.setText(_translate("MainWindow", "Overweight 25 - 30"))
        self.label_7.setText(_translate("MainWindow", "Obese > 30"))
        self.label_8.setText(_translate("MainWindow", "Untits"))
        self.selectUnitButton.setText(_translate("MainWindow", "select unit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionHowUse.setText(_translate("MainWindow", "How to use"))
        
