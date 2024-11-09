from PyQt6 import QtCore, QtGui, QtWidgets


class ui_debt:
    def __init__(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.mainwindow.setObjectName("MainWindow")
        self.mainwindow.setWindowTitle( "Debt Manager")
        self.mainwindow.resize(598, 350)
        self.mainwindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.mainwindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.centralwidget = QtWidgets.QWidget(parent=self.mainwindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.948, y1:1, x2:0, y2:0, stop:0 rgba(195, 166, 0, 255), stop:1 rgba(0, 199, 188, 255));\n"
"    border-radius:9px;\n"
"}\n"
"#label{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#label_2,#label_3,#label_4{\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QProgressBar{\n"
"    border-radius:9px;\n"
"    background-color: rgb(206, 255, 208);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:9px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(170, 214, 218, 255), stop:1 rgba(29, 171, 184, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 165, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 365, 591, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 280, 601, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(80, 240, 431, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)
        self.mainwindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MANAGE</span> YOUR DEBT</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<strong>Created</strong> : AminDev"))
        self.label_4.setText(_translate("MainWindow", "Loading ..."))
        self.label.setText(_translate("MainWindow", "DebtManager"))
