import os

from PyQt6 import QtCore, QtGui, QtWidgets

from translate import lng3

class Ui_Dialog:

    k = 0
    type = 0
    color1 = "#000000"  # 0
    color2 = "#FFFFFF"  # 255
    color3 = "#F0F0F0"  # 240
    color4 = "#E1E1E1"  # 225
    colortext = "#000000"



    def __init__(self):
        self.ln = lng3
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(380, 300)
        self.Dialog.setWindowIcon(
            QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'debt.png')))
        self.Dialog.setWindowTitle("Debt Manager")

        font = QtGui.QFont()
        font.setKerning(True)
        self.Dialog.setFont(font)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

    def Categoryui(self):
        self.widget_3 = QtWidgets.QWidget(parent=self.Dialog)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.frame_12 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_15.setMinimumSize(QtCore.QSize(80, 0))
        self.label_15.setSizeIncrement(QtCore.QSize(60, 0))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.description_3 = QtWidgets.QLineEdit(parent=self.frame_12)
        self.description_3.setObjectName("description_3")
        self.horizontalLayout_12.addWidget(self.description_3)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_6 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.date_3 = QtWidgets.QLineEdit(parent=self.frame_6)
        self.date_3.setObjectName("date_3")
        self.horizontalLayout_6.addWidget(self.date_3)
        self.verticalLayout_4.addWidget(self.frame_6)

        self.verticalLayout.addWidget(self.widget_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.Dialog)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        _translate = QtCore.QCoreApplication.translate
        self.label_14.setText(_translate("Dialog", self.ln[0][self.k]))
        self.label_15.setText(_translate("Dialog", self.ln[1][self.k]))
        self.label_7.setText(_translate("Dialog", self.ln[2][self.k]))
        self.buttonBox.accepted.connect(self.Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def Personui(self):
        self.widget_2 = QtWidgets.QWidget(parent=self.Dialog)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.frame_7 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setSizeIncrement(QtCore.QSize(60, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.description_2 = QtWidgets.QLineEdit(parent=self.frame_7)
        self.description_2.setObjectName("description_2")
        self.horizontalLayout_7.addWidget(self.description_2)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.date_2 = QtWidgets.QLineEdit(parent=self.frame_5)
        self.date_2.setObjectName("date_2")
        self.horizontalLayout_5.addWidget(self.date_2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.amount_2 = QtWidgets.QLineEdit(parent=self.frame_8)
        self.amount_2.setObjectName("amount_2")
        self.horizontalLayout_8.addWidget(self.amount_2)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_12.setMinimumSize(QtCore.QSize(80, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.amount_4 = QtWidgets.QLineEdit(parent=self.frame_9)
        self.amount_4.setObjectName("amount_4")
        self.horizontalLayout_10.addWidget(self.amount_4)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_10)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_11.addWidget(self.comboBox)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.widget_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.Dialog)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(("Dialog"))

        self.label_10.setText(_translate("Dialog", self.ln[4][self.k]))
        self.label_8.setText(_translate("Dialog", self.ln[5][self.k]))
        self.label_6.setText(_translate("Dialog", self.ln[6][self.k]))
        self.label_9.setText(_translate("Dialog", self.ln[7][self.k]))
        self.label_12.setText(_translate("Dialog", self.ln[8][self.k]))
        self.label_13.setText(_translate("Dialog", self.ln[9][self.k]))
        self.buttonBox.accepted.connect(self.Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def Debtui(self):
        self.widget = QtWidgets.QWidget(parent=self.Dialog)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setSizeIncrement(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.description = QtWidgets.QLineEdit(parent=self.frame)
        self.description.setObjectName("description")
        self.horizontalLayout.addWidget(self.description)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(parent=self.widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.date = QtWidgets.QLineEdit(parent=self.frame_3)
        self.date.setObjectName("date")
        self.horizontalLayout_2.addWidget(self.date)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.amount = QtWidgets.QLineEdit(parent=self.frame_2)
        self.amount.setObjectName("amount")
        self.horizontalLayout_3.addWidget(self.amount)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.Dialog)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        _translate = QtCore.QCoreApplication.translate

        self.label_4.setText(_translate("Dialog", self.ln[10][self.k]))
        self.label.setText(_translate("Dialog", self.ln[11][self.k]))
        self.label_2.setText(_translate("Dialog", self.ln[12][self.k]))
        self.label_3.setText(_translate("Dialog", self.ln[13][self.k]))
        self.buttonBox.accepted.connect(self.Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def UpdateStyleSheet(self):
        self.Dialog.setStyleSheet("QFrame{border:0px;}\n"
                                 "QWidget,QFrame,QDialog{\n"
                                 f"    background-color: {self.color4};\n"
                                 "}\n"
                                 "QLineEdit,QComboBox,QTextEdit{\n"
                                 f"    background-color: {self.color3};\n"
                                 f"    color:{self.colortext};\n"
                                 "    border-radius:8px;\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 f"    color:{self.colortext};\n"
                                 f"    background-color: {self.color3};\n"
                                 "\n"
                                 "}\n"
                                 "QLabel{\n"
                                 f"        color:{self.colortext};\n"
                                 "}\n"
                                 "")



