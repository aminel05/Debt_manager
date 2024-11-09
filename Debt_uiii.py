import os
import time

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPainter, QCursor, QColor
from PyQt6.QtWidgets import QVBoxLayout

from translate import lng
from DebtLoadingpage import ui_debt


class Ui_mainWindow(object):
    iconespath = ["custom", "black", "white"]
    iconepath = iconespath[0]

    color1 = "#000000" #0
    color2 = "#FFFFFF" #255
    color3 = "#F0F0F0" #240
    color4 = "#E1E1E1" #225
    color5 = "#EEF3F5"
    colortext = "#000000"
    colort = "#FFFFFF"
    lng = lng
    k = 0
    c = 0
    total1 = 0
    total2 = 0
    total3 = 0

    def setupUi(self, mainWindow):
        self.loadpage = ui_debt()
        QtWidgets.QApplication.processEvents()

        self.updateprogressBar(0,"Ui 1/4")
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1314, 845)
        mainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'debt.png')))
        mainWindow.setWindowTitle("Debt Manager")
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_8 = QtWidgets.QWidget(parent=self.centralwidget)

        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 20, 0, 10)
        self.menubutton2 = QtWidgets.QPushButton(parent=self.widget_8)
        self.menubutton2.setMinimumSize(QtCore.QSize(0, 25))

        self.menubutton2.setObjectName("menubutton2")
        self.verticalLayout_7.addWidget(self.menubutton2)
        self.frame_5 = QtWidgets.QFrame(parent=self.widget_8)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 40, 0, 20)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_5)

        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.homebutton = QtWidgets.QPushButton(parent=self.frame_5)
        self.homebutton.setMinimumSize(QtCore.QSize(0, 25))

        self.homebutton.setObjectName("homebutton")
        self.verticalLayout_6.addWidget(self.homebutton)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_5)

        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.trashbutton = QtWidgets.QPushButton(parent=self.frame_5)
        self.trashbutton.setMinimumSize(QtCore.QSize(0, 25))

        self.trashbutton.setObjectName("trashbutton")
        self.verticalLayout_6.addWidget(self.trashbutton)
        self.verticalLayout_7.addWidget(self.frame_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.frame_6 = QtWidgets.QFrame(parent=self.widget_8)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_6)

        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_8.addWidget(self.pushButton_4)
        self.helpbutton = QtWidgets.QPushButton(parent=self.frame_6)
        self.helpbutton.setMinimumSize(QtCore.QSize(0, 25))

        self.helpbutton.setObjectName("helpbutton")
        self.verticalLayout_8.addWidget(self.helpbutton)
        self.settingbutton = QtWidgets.QPushButton(parent=self.frame_6)
        self.settingbutton.setMinimumSize(QtCore.QSize(0, 25))
        self.settingbutton.setObjectName("settingbutton")
        self.verticalLayout_8.addWidget(self.settingbutton)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.widget_8)
        self.settingswidget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingswidget.sizePolicy().hasHeightForWidth())
        self.settingswidget.setSizePolicy(sizePolicy)
        self.settingswidget.setMinimumSize(QtCore.QSize(0, 0))
        self.settingswidget.setMaximumSize(QtCore.QSize(0, 16777215))

        self.settingswidget.setObjectName("settingswidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.settingswidget)
        self.verticalLayout_14.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.closesettingbutton = QtWidgets.QPushButton(parent=self.settingswidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closesettingbutton.sizePolicy().hasHeightForWidth())
        self.closesettingbutton.setSizePolicy(sizePolicy)
        self.closesettingbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.closesettingbutton.setFont(font)

        self.closesettingbutton.setCheckable(False)
        self.closesettingbutton.setObjectName("closesettingbutton")
        self.verticalLayout_14.addWidget(self.closesettingbutton)
        self.settingstackedwidget = QtWidgets.QStackedWidget(parent=self.settingswidget)
        self.settingstackedwidget.setObjectName("settingstackedwidget")
        self.mainsettingspage = QtWidgets.QWidget()
        self.mainsettingspage.setObjectName("mainsettingspage")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.mainsettingspage)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.settingcontainerwidget = QtWidgets.QWidget(parent=self.mainsettingspage)
        self.settingcontainerwidget.setObjectName("settingcontainerwidget")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.settingcontainerwidget)
        self.verticalLayout_20.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_20.setSpacing(12)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_7 = QtWidgets.QFrame(parent=self.settingcontainerwidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.styleframe = QtWidgets.QFrame(parent=self.frame_7)
        self.styleframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.styleframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.styleframe.setObjectName("styleframe")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.styleframe)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.stylelabel = QtWidgets.QLabel(parent=self.styleframe)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.stylelabel.setFont(font)
        self.stylelabel.setObjectName("stylelabel")
        self.horizontalLayout_12.addWidget(self.stylelabel, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.stylecombobox = QtWidgets.QComboBox(parent=self.styleframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.stylecombobox.sizePolicy().hasHeightForWidth())
        self.stylecombobox.setSizePolicy(sizePolicy)
        self.stylecombobox.setMinimumSize(QtCore.QSize(0, 20))
        self.stylecombobox.setObjectName("stylecombobox")
        self.stylecombobox.addItem("")
        self.stylecombobox.addItem("")
        self.stylecombobox.addItem("")
        self.horizontalLayout_12.addWidget(self.stylecombobox)
        self.verticalLayout_17.addWidget(self.styleframe)
        self.colorswidget = QtWidgets.QWidget(parent=self.frame_7)

        self.colorswidget.setObjectName("colorswidget")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.colorswidget)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.colorlabel1 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel1.setText("")
        self.colorlabel1.setObjectName("colorlabel1")
        self.horizontalLayout_25.addWidget(self.colorlabel1)
        self.colorlabel2 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel2.setText("")
        self.colorlabel2.setObjectName("colorlabel2")
        self.horizontalLayout_25.addWidget(self.colorlabel2)
        self.colorlabel3 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel3.setText("")
        self.colorlabel3.setObjectName("colorlabel3")
        self.horizontalLayout_25.addWidget(self.colorlabel3)
        self.colorlabel4 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel4.setText("")
        self.colorlabel4.setObjectName("colorlabel4")
        self.horizontalLayout_25.addWidget(self.colorlabel4)
        self.colorlabel5 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel5.setText("")
        self.colorlabel5.setObjectName("colorlabel5")
        self.horizontalLayout_25.addWidget(self.colorlabel5)
        self.colorlabel6 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel6.setText("")
        self.colorlabel6.setObjectName("colorlabel6")
        self.horizontalLayout_25.addWidget(self.colorlabel6)
        self.colorlabel7 = QtWidgets.QPushButton(parent=self.colorswidget)
        self.colorlabel7.setText("")
        self.colorlabel7.setObjectName("colorlabel7")
        self.horizontalLayout_25.addWidget(self.colorlabel7)
        self.verticalLayout_17.addWidget(self.colorswidget)
        self.iconframe = QtWidgets.QFrame(parent=self.frame_7)
        self.iconframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.iconframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.iconframe.setObjectName("iconframe")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.iconframe)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.iconslabel = QtWidgets.QLabel(parent=self.iconframe)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.iconslabel.setFont(font)
        self.iconslabel.setObjectName("iconslabel")
        self.horizontalLayout_27.addWidget(self.iconslabel, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.iconsecombobox = QtWidgets.QComboBox(parent=self.iconframe)
        self.iconsecombobox.setObjectName("iconsecombobox")
        self.iconsecombobox.addItem("")
        self.iconsecombobox.addItem("")
        self.iconsecombobox.addItem("")
        self.horizontalLayout_27.addWidget(self.iconsecombobox)
        self.verticalLayout_17.addWidget(self.iconframe)
        self.languageframe = QtWidgets.QFrame(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.languageframe.setFont(font)
        self.languageframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.languageframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.languageframe.setObjectName("languageframe")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.languageframe)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.langyagelabel = QtWidgets.QLabel(parent=self.languageframe)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.langyagelabel.setFont(font)
        self.langyagelabel.setObjectName("langyagelabel")
        self.horizontalLayout_13.addWidget(self.langyagelabel, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.languagecombobox = QtWidgets.QComboBox(parent=self.languageframe)
        self.languagecombobox.setMinimumSize(QtCore.QSize(0, 20))
        self.languagecombobox.setObjectName("languagecombobox")
        self.languagecombobox.addItem("")
        self.languagecombobox.addItem("")
        self.languagecombobox.addItem("")
        self.horizontalLayout_13.addWidget(self.languagecombobox)
        self.verticalLayout_17.addWidget(self.languageframe)

        self.curencyframe = QtWidgets.QFrame(parent=self.frame_7)
        self.curencyframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.curencyframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.curencyframe.setObjectName("curencyframe")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.curencyframe)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.currencylabel = QtWidgets.QLabel(parent=self.curencyframe)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.currencylabel.setFont(font)
        self.currencylabel.setObjectName("currencylabel")
        self.horizontalLayout_19.addWidget(self.currencylabel, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.curencycombobox = QtWidgets.QComboBox(parent=self.curencyframe)
        self.curencycombobox.setMinimumSize(QtCore.QSize(0, 20))
        self.curencycombobox.setObjectName("curencycombobox")
        self.curencycombobox.addItem("")
        self.curencycombobox.addItem("")
        self.curencycombobox.addItem("")
        self.horizontalLayout_19.addWidget(self.curencycombobox)
        self.verticalLayout_17.addWidget(self.curencyframe)
        self.verticalLayout_20.addWidget(self.frame_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_20.addItem(spacerItem1)
        self.verticalLayout_15.addWidget(self.settingcontainerwidget)
        self.createdbcopybutton = QtWidgets.QPushButton(parent=self.mainsettingspage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createdbcopybutton.sizePolicy().hasHeightForWidth())
        self.createdbcopybutton.setSizePolicy(sizePolicy)
        self.createdbcopybutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.createdbcopybutton.setFont(font)

        self.createdbcopybutton.setCheckable(False)
        self.createdbcopybutton.setObjectName("createdbcopybutton")
        self.verticalLayout_15.addWidget(self.createdbcopybutton)
        self.settingstackedwidget.addWidget(self.mainsettingspage)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_31.addItem(spacerItem2)
        self.frame_25 = QtWidgets.QFrame(parent=self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)

        self.frame_25.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_30.addWidget(self.label_9)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.frame_25)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_30.addWidget(self.radioButton_3)
        #self.radioButton_4 = QtWidgets.QRadioButton(parent=self.frame_25)
        #self.radioButton_4.setObjectName("radioButton_4")
        #self.verticalLayout_30.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.frame_25)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_30.addWidget(self.radioButton_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_25)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_30.addWidget(self.lineEdit_5)
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame_25)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_30.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.frame_25)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_30.addWidget(self.checkBox_2)
        self.dbtoxecxel = QtWidgets.QPushButton(parent=self.frame_25)
        self.dbtoxecxel.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.dbtoxecxel.setFont(font)
        self.dbtoxecxel.setObjectName("dbtoxecxel")
        self.verticalLayout_30.addWidget(self.dbtoxecxel)
        self.verticalLayout_31.addWidget(self.frame_25)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_31.addItem(spacerItem3)
        self.settingstackedwidget.addWidget(self.page_5)
        self.helppage = QtWidgets.QWidget()
        self.helppage.setObjectName("helppage")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.helppage)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.help2 = QtWidgets.QTextBrowser(parent=self.helppage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.help2.setFont(font)
        self.help2.setObjectName("help2")
        self.verticalLayout_16.addWidget(self.help2)
        self.help = QtWidgets.QTextBrowser(parent=self.helppage)
        self.help.setObjectName("help")
        self.verticalLayout_16.addWidget(self.help, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.settingstackedwidget.addWidget(self.helppage)
        self.verticalLayout_14.addWidget(self.settingstackedwidget)
        self.horizontalLayout.addWidget(self.settingswidget)
        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)

        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_21.setContentsMargins(9, 0, 9, 9)
        self.verticalLayout_21.setSpacing(15)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_51 = QtWidgets.QFrame(parent=self.widget_4)
        self.frame_51.setObjectName("frame_51")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_51)
        self.horizontalLayout_30.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_51)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 25))

        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_30.addWidget(self.pushButton_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem4)
        self.label_28 = QtWidgets.QLabel(parent=self.frame_51)
        self.label_28.setMaximumSize(QtCore.QSize(80, 80))
        self.label_28.setStyleSheet("padding:0px;\n"
"border-radius:none;")
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'debt.png')))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_30.addWidget(self.label_28)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem5)
        self.label_29 = QtWidgets.QLabel(parent=self.frame_51)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_30.addWidget(self.label_29)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem7)
        self.verticalLayout_21.addWidget(self.frame_51)
        self.line = QtWidgets.QFrame(parent=self.widget_4)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_21.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget = QtWidgets.QWidget(parent=self.page)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_52 = QtWidgets.QFrame(parent=self.widget)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        ##################
        self.frame_logo4 = QtWidgets.QFrame(parent=self.frame_52)
        self.frame_logo4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo4.setObjectName("frame_logo4")
        self.frame_logo4.setMaximumHeight(40)
        self.horizontalLayout_frame_logo4 = QtWidgets.QHBoxLayout(self.frame_logo4)
        self.horizontalLayout_frame_logo4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo4.setObjectName("horizontalLayout_frame_logo4")
        self.horizontalLayout_frame_logo4.setSpacing(0)

        ##################
        self.label_5logo = QtWidgets.QLabel(parent=self.frame_logo4)
        self.label_5logo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'man-avatar.png')))
        self.label_5logo.setScaledContents(True)
        self.label_5logo.setObjectName("label_32logo")
        self.label_5logo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo4.addWidget(self.label_5logo)


        self.label_5 = QtWidgets.QLabel(parent=self.frame_logo4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_frame_logo4.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.frame_logo4)

        self.frame_4 = QtWidgets.QFrame(parent=self.frame_52)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setContentsMargins(9, 0, 0, 1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setSpacing(0)
        self.searchbutton = QtWidgets.QPushButton(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbutton.sizePolicy().hasHeightForWidth())
        self.searchbutton.setSizePolicy(sizePolicy)
        self.searchbutton.setMinimumSize(QtCore.QSize(0, 0))
        self.searchbutton.setStyleSheet("background-color:transparent;")
        self.searchbutton.setText("")

        self.searchbutton.setObjectName("searchbutton")
        self.horizontalLayout_7.addWidget(self.searchbutton)
        self.updateprogressBar(10, "Ui 2/4")
        self.searchlineedit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.searchlineedit.setObjectName("searchlineedit")
        self.horizontalLayout_7.addWidget(self.searchlineedit)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.peapoletable = QtWidgets.QTableWidget(parent=self.frame_52)
        self.peapoletable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.peapoletable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.peapoletable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.peapoletable.setObjectName("peapoletable")
        self.peapoletable.setColumnCount(8)
        self.peapoletable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable.setHorizontalHeaderItem(7, item)
        self.peapoletable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.peapoletable)
        self.widget_6 = QtWidgets.QWidget(parent=self.frame_52)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addpersonbutton = QtWidgets.QPushButton(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addpersonbutton.sizePolicy().hasHeightForWidth())
        self.addpersonbutton.setSizePolicy(sizePolicy)
        self.addpersonbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.addpersonbutton.setFont(font)

        self.addpersonbutton.setObjectName("addpersonbutton")
        self.horizontalLayout_6.addWidget(self.addpersonbutton)
        self.removepersonbutton = QtWidgets.QPushButton(parent=self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removepersonbutton.sizePolicy().hasHeightForWidth())
        self.removepersonbutton.setSizePolicy(sizePolicy)
        self.removepersonbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.removepersonbutton.setFont(font)

        self.removepersonbutton.setObjectName("removepersonbutton")
        self.horizontalLayout_6.addWidget(self.removepersonbutton)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_5.addWidget(self.frame_52)
        self.horizontalLayout_8.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=self.page)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2.setMaximumSize(QtCore.QSize(600, 16777215))

        self.frame_41 = QtWidgets.QFrame(parent=self.widget_2)

        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_17.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_41.setMaximumHeight(280)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem8)
        self.frame_15 = QtWidgets.QFrame(parent=self.frame_41)
        self.frame_15.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_13.addWidget(self.label_12)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_15)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame_10)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_14.addWidget(self.lineEdit_7)
        self.verticalLayout_13.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_15)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.frame_12)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_16.addWidget(self.lineEdit_9)
        self.verticalLayout_13.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_15)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_15.addWidget(self.label_14, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_15.addWidget(self.lineEdit_8)
        self.verticalLayout_13.addWidget(self.frame_11)
        self.frame_21 = QtWidgets.QFrame(parent=self.frame_15)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_26 = QtWidgets.QLabel(parent=self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_32.addWidget(self.label_26, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.frame_21)
        self.lineEdit_10.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_32.addWidget(self.lineEdit_10)
        self.verticalLayout_13.addWidget(self.frame_21)
        self.frame_18 = QtWidgets.QFrame(parent=self.frame_15)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_27 = QtWidgets.QLabel(parent=self.frame_18)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_28.addWidget(self.label_27, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_18)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_28.addWidget(self.comboBox)
        self.verticalLayout_13.addWidget(self.frame_18)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_3.setFont(font)

        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_13.addWidget(self.pushButton_3)
        self.horizontalLayout_17.addWidget(self.frame_15)
        self.frame_14 = QtWidgets.QFrame(parent=self.frame_41)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_14.setMaximumWidth(0)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.frame = QtWidgets.QFrame(parent=self.frame_14)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout.addWidget(self.frame_3)
        #self.frame_20 = QtWidgets.QFrame(parent=self.frame_14)
        #self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        #self.frame_20.setObjectName("frame_20")
        #self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_20)
        #self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        #spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        #self.horizontalLayout_29.addItem(spacerItem8)
        #self.radioButton = QtWidgets.QRadioButton(parent=self.frame_20)
        #self.radioButton.setChecked(True)
        #self.radioButton.setObjectName("radioButton")
        #self.horizontalLayout_29.addWidget(self.radioButton)
        #self.radioButton_2 = QtWidgets.QRadioButton(parent=self.frame_20)
        #self.radioButton_2.setObjectName("radioButton_2")
        #self.horizontalLayout_29.addWidget(self.radioButton_2)
        #spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        #self.horizontalLayout_29.addItem(spacerItem9)
        #self.verticalLayout.addWidget(self.frame_20)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.updateprogressBar(20, "Ui 3/4")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_17.addWidget(self.frame_14)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem11)
        self.verticalLayout_4.addWidget(self.frame_41)
        self.frame_71 = QtWidgets.QFrame(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy)
        self.frame_71.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_71.setObjectName("frame_71")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_71)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        ##################
        self.frame_logo5 = QtWidgets.QFrame(parent=self.frame_71)
        self.frame_logo5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo5.setObjectName("frame_logo5")
        self.frame_logo5.setMaximumHeight(40)
        self.horizontalLayout_frame_logo5 = QtWidgets.QHBoxLayout(self.frame_logo5)
        self.horizontalLayout_frame_logo5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo5.setObjectName("horizontalLayout_frame_logo5")
        self.horizontalLayout_frame_logo5.setSpacing(0)

        ##################
        self.label_logo = QtWidgets.QLabel(parent=self.frame_logo5)
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'debt2.png')))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_logo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo5.addWidget(self.label_logo)

        self.label = QtWidgets.QLabel(parent=self.frame_71)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_frame_logo5.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_logo5)

        self.debttable = QtWidgets.QTableWidget(parent=self.frame_71)
        self.debttable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debttable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.debttable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.debttable.setRowCount(0)
        self.debttable.setObjectName("debttable")
        self.debttable.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.debttable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.debttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.debttable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.debttable.setHorizontalHeaderItem(3, item)
        self.debttable.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.debttable)
        self.widget_3 = QtWidgets.QWidget(parent=self.frame_71)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.adddebtbutton = QtWidgets.QPushButton(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adddebtbutton.sizePolicy().hasHeightForWidth())
        self.adddebtbutton.setSizePolicy(sizePolicy)
        self.adddebtbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.adddebtbutton.setFont(font)

        self.adddebtbutton.setObjectName("adddebtbutton")
        self.horizontalLayout_5.addWidget(self.adddebtbutton)
        self.removedebtbutton = QtWidgets.QPushButton(parent=self.widget_3)
        self.removedebtbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.removedebtbutton.setFont(font)

        self.removedebtbutton.setObjectName("removedebtbutton")
        self.horizontalLayout_5.addWidget(self.removedebtbutton)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.frame_71)
        self.horizontalLayout_8.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(15)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.widget_22 = QtWidgets.QWidget(parent=self.page_4)
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_9 = QtWidgets.QFrame(parent=self.widget_22)

        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_24.setSpacing(15)
        self.verticalLayout_24.setObjectName("verticalLayout_24")

        ##################
        self.frame_logo = QtWidgets.QFrame(parent=self.frame_9)
        self.frame_logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo.setObjectName("frame_4")
        self.frame_logo.setMaximumHeight(40)
        self.horizontalLayout_frame_logo = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_frame_logo.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo.setObjectName("horizontalLayout_frame_logo")
        self.horizontalLayout_frame_logo.setSpacing(0)

        ##################
        self.label_25logo = QtWidgets.QLabel(parent=self.frame_logo)
        self.label_25logo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'shapes.png')))
        self.label_25logo.setScaledContents(True)
        self.label_25logo.setObjectName("label_25")
        self.label_25logo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo.addWidget(self.label_25logo)

        self.label_25 = QtWidgets.QLabel(parent=self.frame_logo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_frame_logo.addWidget(self.label_25)
        self.verticalLayout_24.addWidget(self.frame_logo)
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.frame_9)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.verticalLayout_24.addWidget(self.tableWidget_3)
        self.widget_19 = QtWidgets.QWidget(parent=self.frame_9)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_24.addWidget(self.widget_19)
        self.label_22 = QtWidgets.QLabel(parent=self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_24.addWidget(self.label_22)
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_23 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_22.addWidget(self.label_23,0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_22.addWidget(self.lineEdit_4)
        self.verticalLayout_24.addWidget(self.frame_13)
        self.frame_16 = QtWidgets.QFrame(parent=self.frame_9)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_16)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_24.addWidget(self.label_24, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(400, 80))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_24.addWidget(self.textEdit)
        self.verticalLayout_24.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(parent=self.frame_9)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_9.setFont(font)

        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_26.addWidget(self.pushButton_9)

        self.pushButton_92 = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_92.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_92.setFont(font)

        self.pushButton_92.setObjectName("pushButton_92")
        self.horizontalLayout_26.addWidget(self.pushButton_92)


        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_26.addWidget(self.pushButton_10)
        self.verticalLayout_24.addWidget(self.frame_17)
        self.verticalLayout_23.addWidget(self.frame_9)
        self.horizontalLayout_23.addWidget(self.widget_22)
        self.widget_18 = QtWidgets.QWidget(parent=self.page_4)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_19 = QtWidgets.QFrame(parent=self.widget_18)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_26.setSpacing(15)
        self.verticalLayout_26.setObjectName("verticalLayout_26")

        ##################
        self.frame_logo2 = QtWidgets.QFrame(parent=self.frame_19)
        self.frame_logo2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo2.setObjectName("frame_logo2")
        self.frame_logo2.setMaximumHeight(40)
        self.horizontalLayout_frame_logo2 = QtWidgets.QHBoxLayout(self.frame_logo2)
        self.horizontalLayout_frame_logo2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo2.setObjectName("horizontalLayout_frame_logo2")
        self.horizontalLayout_frame_logo2.setSpacing(0)

        ##################
        self.label_21logo = QtWidgets.QLabel(parent=self.frame_logo2)
        self.label_21logo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'man-avatar.png')))
        self.label_21logo.setScaledContents(True)
        self.label_21logo.setObjectName("label_21logo")
        self.label_21logo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo2.addWidget(self.label_21logo)

        self.label_21 = QtWidgets.QLabel(parent=self.frame_logo2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_frame_logo2.addWidget(self.label_21)
        self.verticalLayout_26.addWidget(self.frame_logo2)

        self.peapoletable_2 = QtWidgets.QTableWidget(parent=self.frame_19)
        self.peapoletable_2.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.peapoletable_2.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.peapoletable_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.peapoletable_2.setObjectName("peapoletable_2")
        self.peapoletable_2.setColumnCount(7)
        self.peapoletable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.peapoletable_2.setHorizontalHeaderItem(6, item)

        self.peapoletable_2.verticalHeader().setVisible(False)
        self.verticalLayout_26.addWidget(self.peapoletable_2)
        self.widget_20 = QtWidgets.QWidget(parent=self.frame_19)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(9)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.addpersonbutton_2 = QtWidgets.QPushButton(parent=self.widget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addpersonbutton_2.sizePolicy().hasHeightForWidth())
        self.addpersonbutton_2.setSizePolicy(sizePolicy)
        self.addpersonbutton_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.addpersonbutton_2.setFont(font)

        self.addpersonbutton_2.setObjectName("addpersonbutton_2")
        self.horizontalLayout_21.addWidget(self.addpersonbutton_2)
        self.removepersonbutton_2 = QtWidgets.QPushButton(parent=self.widget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removepersonbutton_2.sizePolicy().hasHeightForWidth())
        self.removepersonbutton_2.setSizePolicy(sizePolicy)
        self.removepersonbutton_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.removepersonbutton_2.setFont(font)

        self.removepersonbutton_2.setObjectName("removepersonbutton_2")
        self.horizontalLayout_21.addWidget(self.removepersonbutton_2)
        self.verticalLayout_26.addWidget(self.widget_20)
        self.verticalLayout_19.addWidget(self.frame_19)
        self.frame_23 = QtWidgets.QFrame(parent=self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_25.setSpacing(15)
        self.verticalLayout_25.setObjectName("verticalLayout_25")

        ##################
        self.frame_logo3 = QtWidgets.QFrame(parent=self.frame_23)
        self.frame_logo3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo3.setObjectName("frame_logo3")
        self.frame_logo3.setMaximumHeight(40)
        self.horizontalLayout_frame_logo3 = QtWidgets.QHBoxLayout(self.frame_logo3)
        self.horizontalLayout_frame_logo3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo3.setObjectName("horizontalLayout_frame_logo3")
        self.horizontalLayout_frame_logo3.setSpacing(0)

        ##################
        self.label_32logo = QtWidgets.QLabel(parent=self.frame_logo3)
        self.label_32logo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'debt2.png')))
        self.label_32logo.setScaledContents(True)
        self.label_32logo.setObjectName("label_32logo")
        self.label_32logo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo3.addWidget(self.label_32logo)


        self.label_32 = QtWidgets.QLabel(parent=self.frame_23)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_frame_logo3.addWidget(self.label_32)
        self.verticalLayout_25.addWidget(self.frame_logo3)

        self.debttable_2 = QtWidgets.QTableWidget(parent=self.frame_23)
        self.debttable_2.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debttable_2.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.debttable_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.debttable_2.setObjectName("debttable_2")
        self.debttable_2.setColumnCount(4)
        self.debttable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.debttable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.debttable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.debttable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.debttable_2.setHorizontalHeaderItem(3, item)
        self.debttable_2.verticalHeader().setVisible(False)
        self.verticalLayout_25.addWidget(self.debttable_2)
        self.widget_24 = QtWidgets.QWidget(parent=self.frame_23)
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.adddebtbutton_2 = QtWidgets.QPushButton(parent=self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adddebtbutton_2.sizePolicy().hasHeightForWidth())
        self.adddebtbutton_2.setSizePolicy(sizePolicy)
        self.adddebtbutton_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.adddebtbutton_2.setFont(font)

        self.adddebtbutton_2.setObjectName("adddebtbutton_2")
        self.horizontalLayout_31.addWidget(self.adddebtbutton_2)
        self.removedebtbutton_2 = QtWidgets.QPushButton(parent=self.widget_24)
        self.removedebtbutton_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.removedebtbutton_2.setFont(font)

        self.removedebtbutton_2.setObjectName("removedebtbutton_2")
        self.horizontalLayout_31.addWidget(self.removedebtbutton_2)
        self.verticalLayout_25.addWidget(self.widget_24)
        self.verticalLayout_19.addWidget(self.frame_23)
        self.horizontalLayout_23.addWidget(self.widget_18)
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.widget_14 = QtWidgets.QWidget(parent=self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.948, y1:1, x2:0, y2:0, stop:0 rgba(195, 166, 0, 255), stop:1 rgba(0, 199, 188, 255));\n"
"color:white;\n"
"padding:10px;")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_18.addWidget(self.label_11)
        self.label_17 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.994, y1:0.607955, x2:0, y2:0.960227, stop:0 rgba(181, 0, 62, 255), stop:1 rgba(78, 201, 255, 255));\n"
"color:white;\n"
"padding:10px;")
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.545, y2:0, stop:0 rgba(239, 212, 67, 255), stop:1 rgba(208, 114, 175, 255));\n"
"color:white;\n"
"padding:10px;")
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.verticalLayout_22.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(parent=self.page_3)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_33.setSpacing(15)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.widget_16 = QtWidgets.QWidget(parent=self.widget_15)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(15)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_22 = QtWidgets.QWidget(parent=self.widget_16)
        #self.frame_22.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_22.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_22.setObjectName("frame_22")

        self.verticalLayout_18.addWidget(self.frame_22)
        self.frame_24 = QtWidgets.QFrame(parent=self.widget_16)
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_29.setObjectName("verticalLayout_29")

        ##################
        self.frame_logo7 = QtWidgets.QFrame(parent=self.frame_24)
        self.frame_logo7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo7.setObjectName("frame_logo7")
        self.frame_logo7.setMaximumHeight(40)
        self.horizontalLayout_frame_logo7 = QtWidgets.QHBoxLayout(self.frame_logo7)
        self.horizontalLayout_frame_logo7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo7.setObjectName("horizontalLayout_frame_logo4")
        self.horizontalLayout_frame_logo7.setSpacing(0)

        ##################
        self.label_20ogo = QtWidgets.QLabel(parent=self.frame_logo7)
        self.label_20ogo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'history2.png')))
        self.label_20ogo.setScaledContents(True)
        self.label_20ogo.setObjectName("label_20ogo")
        self.label_20ogo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo7.addWidget(self.label_20ogo)

        self.updateprogressBar(30, "Ui 4/4")
        self.label_20 = QtWidgets.QLabel(parent=self.frame_logo7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_frame_logo7.addWidget(self.label_20)
        self.verticalLayout_29.addWidget(self.frame_logo7)

        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.frame_24)
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.verticalLayout_29.addWidget(self.tableWidget_2)
        self.verticalLayout_18.addWidget(self.frame_24)
        self.horizontalLayout_33.addWidget(self.widget_16)
        self.frame_171 = QtWidgets.QFrame(parent=self.widget_15)
        self.frame_171.setObjectName("frame_171")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_171)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        #self.label_8 = QtWidgets.QLabel(parent=self.frame_171)
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #font.setBold(True)
        #self.label_8.setFont(font)
        #self.label_8.setObjectName("label_8")
        #self.verticalLayout_27.addWidget(self.label_8)
        self.graphicsView = QtWidgets.QWidget(parent=self.frame_171)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_27.addWidget(self.graphicsView)
        self.horizontalLayout_33.addWidget(self.frame_171)
        self.verticalLayout_22.addWidget(self.widget_15)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_10 = QtWidgets.QWidget(parent=self.page_2)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_131 = QtWidgets.QFrame(parent=self.widget_10)
        self.frame_131.setObjectName("frame_131")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_131)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        ##################
        self.frame_logo6 = QtWidgets.QFrame(parent=self.frame_131)
        self.frame_logo6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo6.setObjectName("frame_logo6")
        self.frame_logo6.setMaximumHeight(40)
        self.horizontalLayout_frame_logo6 = QtWidgets.QHBoxLayout(self.frame_logo6)
        self.horizontalLayout_frame_logo6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_frame_logo6.setObjectName("horizontalLayout_frame_logo6")
        self.horizontalLayout_frame_logo6.setSpacing(0)

        ##################
        self.label_16logo = QtWidgets.QLabel(parent=self.frame_logo6)
        self.label_16logo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icones', 'custom', 'recycle-bin.png')))
        self.label_16logo.setScaledContents(True)
        self.label_16logo.setObjectName("label_logo")
        self.label_16logo.setMaximumWidth(60)
        self.horizontalLayout_frame_logo6.addWidget(self.label_16logo)


        self.label_16 = QtWidgets.QLabel(parent=self.frame_logo6)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_frame_logo6.addWidget(self.label_16)
        self.verticalLayout_12.addWidget(self.frame_logo6)

        self.deletedtable = QtWidgets.QTableWidget(parent=self.frame_131)
        self.deletedtable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.deletedtable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.deletedtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.deletedtable.setObjectName("deletedtable")
        self.deletedtable.setColumnCount(8)
        self.deletedtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.deletedtable.setHorizontalHeaderItem(7, item)
        self.deletedtable.verticalHeader().setVisible(False)
        self.deletedtable.verticalHeader().setDefaultSectionSize(40)
        self.verticalLayout_12.addWidget(self.deletedtable)
        self.widget_9 = QtWidgets.QWidget(parent=self.frame_131)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.deletebutton = QtWidgets.QPushButton(parent=self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletebutton.sizePolicy().hasHeightForWidth())
        self.deletebutton.setSizePolicy(sizePolicy)
        self.deletebutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.deletebutton.setFont(font)

        self.deletebutton.setObjectName("deletebutton")
        self.horizontalLayout_9.addWidget(self.deletebutton)
        self.recoverbutton = QtWidgets.QPushButton(parent=self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recoverbutton.sizePolicy().hasHeightForWidth())
        self.recoverbutton.setSizePolicy(sizePolicy)
        self.recoverbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.recoverbutton.setFont(font)

        self.recoverbutton.setObjectName("recoverbutton")
        self.horizontalLayout_9.addWidget(self.recoverbutton)
        self.verticalLayout_12.addWidget(self.widget_9)
        self.verticalLayout_9.addWidget(self.frame_131)
        self.horizontalLayout_10.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(parent=self.page_2)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_121 = QtWidgets.QFrame(parent=self.widget_11)
        self.frame_121.setObjectName("frame_121")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_121)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.deleteallbutton = QtWidgets.QPushButton(parent=self.frame_121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteallbutton.sizePolicy().hasHeightForWidth())
        self.deleteallbutton.setSizePolicy(sizePolicy)
        self.deleteallbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.deleteallbutton.setFont(font)

        self.deleteallbutton.setObjectName("deleteallbutton")
        self.verticalLayout_11.addWidget(self.deleteallbutton)
        self.recoverallbutton = QtWidgets.QPushButton(parent=self.frame_121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recoverallbutton.sizePolicy().hasHeightForWidth())
        self.recoverallbutton.setSizePolicy(sizePolicy)
        self.recoverallbutton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        self.recoverallbutton.setFont(font)

        self.recoverallbutton.setObjectName("recoverallbutton")
        self.verticalLayout_11.addWidget(self.recoverallbutton)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem10)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_121)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout_10.addWidget(self.frame_121)
        self.horizontalLayout_10.addWidget(self.widget_11)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_21.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.widget_4)
        mainWindow.setCentralWidget(self.centralwidget)
        self.updateprogressBar(50, "Charts")
        #piechart
        self.series = QPieSeries()
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.layoutchart = QVBoxLayout()
        self.layoutchart.addWidget(self.chart_view)
        self.graphicsView.setLayout(self.layoutchart)
        #barchart

        self.barseries = QBarSeries()
        self.barchart = QChart()
        self.barchart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.barchart_view = QChartView(self.barchart)
        self.barchart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.bar_axisX = QBarCategoryAxis()
        self.bar_axisY1 = QValueAxis()
        self.barlayout = QVBoxLayout()
        self.barlayout.addWidget(self.barchart_view)
        self.frame_22.setLayout(self.barlayout)
        self.barchart.addSeries(self.barseries)


        self.tooltip_label = QtWidgets.QLabel()
        self.tooltip_label.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000;")
        self.tooltip_label.setWindowFlags(Qt.WindowType.ToolTip)  # Makes it act like a tooltip
        self.tooltip_label.setFont(QtGui.QFont("Arial", 10))
        self.tooltip_label.hide()

        self.updateprogressBar(60, "Translation")
        self.retranslateUi()
        self.settingstackedwidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def updateprogressBar(self,value,text):
        while(self.loadpage.progressBar.value()<value):
            time.sleep(0.01)
            self.loadpage.progressBar.setValue(self.loadpage.progressBar.value()+1)
        self.loadpage.label_4.setText(f"Loading {text}")

    def barcharttt(self,data):
        self.set0 = QBarSet(lng[65][self.k])
        self.set0.setColor(QColor("#01D5D5"))

        self.bar_axisX.clear()

        highest_debt = 0
        for value in data:
            self.set0.append(float(value[1]))

            self.bar_axisX.append(value[0])

            if value[1]> highest_debt:highest_debt = value[1]

        self.barseries.clear()
        self.barseries.append(self.set0)


        maxrange = (round(round(highest_debt)/500)+1)*500

        self.bar_axisY1.setRange(0, maxrange)
        self.bar_axisY1.setTitleText(self.curencycombobox.currentText())

        #self.barchart.removeAllSeries()
        self.barchart.removeAxis(self.bar_axisY1)
        self.barchart.removeAxis(self.bar_axisX)

        self.barchart.addAxis(self.bar_axisY1, Qt.AlignmentFlag.AlignLeft)

        self.barseries.attachAxis(self.bar_axisY1)

        self.barchart.addAxis(self.bar_axisX, Qt.AlignmentFlag.AlignBottom)
        self.barseries.attachAxis(self.bar_axisX)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.barchart.setTitleFont(font)
        for bar_set in self.barseries.barSets():
            bar_set.setBorderColor(QColor(self.color2))
            bar_set.hovered.connect(self.on_bar_hover)

    def chartt(self,data):
        # Create a pie series
        self.series.clear()
        self.slices = []
        start_r, start_g, start_b = (26,208,197)
        end_r, end_g, end_b = (219,218,11)
        colors = []
        count = len(data)+1
        for i in range(count):
            r = int(start_r + (end_r - start_r) * (i / (count - 1)))
            g = int(start_g + (end_g - start_g) * (i / (count - 1)))
            b = int(start_b + (end_b - start_b) * (i / (count - 1)))
            colors.append(f"#{r:02X}{g:02X}{b:02X}")


        for index,value in enumerate(data):
            slice_ = self.series.append(value[0], value[1])
            self.slices.append(slice_)
            slice_.setColor(QColor(colors[index]))
            slice_.setBorderColor(Qt.GlobalColor.transparent)
            slice_.setExploded(True)
            slice_.setExplodeDistanceFactor(0.01)
            slice_.hovered.connect(lambda state, s=slice_: self.on_slice_hovered(state, s))

        # Create the chart and add the series

        #self.chart.removeAllSeries()
        self.chart.addSeries(self.series)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)

        for i in self.slices: i.setBorderColor(QColor(self.color2))

        self.chart.setTitleFont(font)
        self.graphicsView.update()

    def on_bar_hover(self,state,bar_set):
        try:
            if state:
                value = self.set0[bar_set]
                tooltip_text = f" {value} {self.curencycombobox.currentText()} "
                self.tooltip_label.setText(tooltip_text)
                self.tooltip_label.move(QCursor.pos())
                self.tooltip_label.show()
            else:  # When the mouse leaves the slice
                self.tooltip_label.hide()
        except Exception as e:
            print(str(e))

    def on_slice_hovered(self, state, slice_):
        if state:  # When the mouse enters the slice
            percentage = slice_.percentage() * 100
            tooltip_text = f"{slice_.label()}: {slice_.value()} {self.curencycombobox.currentText()} ({percentage:.2f}%)"
            #QToolTip.showText(QCursor.pos(), tooltip_text)
            self.tooltip_label.setText(tooltip_text)
            self.tooltip_label.move(QCursor.pos())
            self.tooltip_label.show()
            slice_.setExplodeDistanceFactor(0.15)
        else:  # When the mouse leaves the slice
            self.tooltip_label.hide()
            slice_.setExplodeDistanceFactor(0.01)

    def UpdateStyleSheet(self):
            self.centralwidget.setStyleSheet("#centralwidget{\n"
                                             "    \n"
                                             f"    background-color: {self.color5};\n"
                                             "}\n"
                                             "QPushButton::hover{\n"
                                             "    \n"
                                             "    background-color: rgb(184, 218, 247);\n"
                                             "}")
            self.widget_8.setStyleSheet("QWidget{\n"
                                        f"    background-color: {self.color1};\n"
                                        "\n"
                                        "}\n"
                                        "QFrame{border : 0px;}"
                                        "QPushButton{\n"
                                        "    border-radius:7px;\n"
                                        "    min-height:25px;\n"
                                        "    font-weight:bold;\n"
                                        f"    color: {self.colort};\n"
                                        "    padding-left:10px;\n"
                                        "    padding-right:10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(193, 210, 255);\n"
                                        "}")
            self.settingswidget.setStyleSheet("#settingswidget{\n"
                                              f"    background-color: {self.color3};\n"
                                              f"    border:1px solid {self.color4};\n"
                                              "    border-radius:11px;\n"
                                              "    margin:5px;\n"
                                              "}\n"
                                              "#settingstackedwidget{\n"
                                              f"    background-color: {self.color3};\n"
                                              "}\n"
                                              "QWidget{\n"
                                              "    background-color:transparent;\n"
                                              "}\n"
                                              "QFrame{\n"
                                              f"    background-color: {self.color2};\n"
                                              "    border-radius:9px;\n"
                                              "}\n"
                                              "QPushButton{\n"
                                              f"background-color: {self.color4};\n"
                                              "border-radius : 9px;\n"
                                              f"color:{self.colortext};\n"
                                              "}\n"
                                              "QComboBox{\n"
                                              "    padding-left:10px;\n"
                                              f"    background-color: {self.color4};"
                                              f"   border:1px solid {self.color4};"
                                              "border-radius:9px;"
                                              f"color:{self.colortext};\n"
                                              "}\n"
                                              "QComboBox::drop-down {\n"
                                              "    border-top-right-radius:8px;\n"
                                              "    border-bottom-right-radius:8px;\n"
                                              f"    border-left:1px solid {self.color2};\n"
                                              "}\n"
                                              f"""QComboBox QAbstractItemView {{
                                              background-color: {self.color4}; 
                                              color: {self.colortext}; 
                                              selection-background-color: rgb(0, 0, 0);}}"""
                                              ""
                                              "QTextEdit{\n"
                                              "border-radius:9px;\n"
                                              f"background-color: {self.color4};\n"
                                              f"color:{self.colortext};\n"
                                              "}\n"
                                              "QPushButton::hover{\n"
                                              "    background-color: rgb(184, 218, 247);\n"
                                              "}\n"
                                              "QLabel{\n"
                                              f"color:{self.colortext};\n"
                                              "background-color:transparent;\n"
                                              "}\n"
                                              "QLineEdit{\n"
                                              "    border-radius:4px;\n"
                                              f"    border:1px solid {self.color4};\n"
                                              "    padding-left:10px;\n"
                                              f"color:{self.colortext};\n"
                                              "}"
                                              f"""QRadioButton,QCheckBox{{color:{self.colortext};\n}}"""
                                              f"""QRadioButton::indicator::unchecked {{
                                              background-color: {self.color2};
                                              border :1px solid{self.color1};
                                              border-radius:6px;
                                              }}"""
                                              f"""QRadioButton::indicator::checked {{
                                                                                      background-color: {self.color1};
                                                                                      border :1px solid{self.color1};
                                                                                      border-radius:5px;
                                                                                      }}"""
                                              )
            self.colorswidget.setStyleSheet("QPushButton{\n"
                                            "    max-height:25px;\n"
                                            "    max-width:25px;\n"
                                            "    min-height:25px;\n"
                                            "    min-width:25px;\n"
                                            "    border-radius:4px;\n"
                                            "    border:1px solid;\n"
                                            "}\n"
                                            "#colorlabel1{\n"
                                            f"    background-color: {self.color1};\n"
                                            "}\n"
                                            "#colorlabel2{\n"
                                            f"    background-color: {self.color2};\n"
                                            "}\n"
                                            "#colorlabel3{\n"
                                            f"    background-color: {self.color3};\n"
                                            "}\n"
                                            "#colorlabel4{\n"
                                            f"    background-color: {self.color4};\n"
                                            "\n"
                                            "}\n"
                                            "#colorlabel5{\n"
                                            f"    background-color: {self.color5};\n"
                                            "}\n"
                                            "#colorlabel6{\n"
                                            f"    background-color: {self.colortext};\n"
                                            "}"
                                            "#colorlabel7{\n"
                                            f"    background-color: {self.colort};\n"
                                            "}"
                                            )
            self.pushButton_8.setStyleSheet("QPushButton{\n"
                                            "    border-radius:8px;\n"
                                            "    background-color: transparent;\n"
                                            "\n"
                                            "}\n"
                                            "QPushButton::hover{\n"
                                            f"    background-color: {self.color3};\n"
                                            "}")
            self.frame_41.setStyleSheet("QLineEdit{\n"
                                        f"    border-bottom:1px solid {self.color4};\n"
                                        "}")
            self.frame_9.setStyleSheet("QLineEdit,QTextEdit{\n"
                                       f"    border-bottom:1px solid {self.color1};\n"
                                       "    padding-left:10px;\n"
                                       "}\n"
                                       "QTextEdit{\n"
                                       f"    border:1px solid {self.color1};\n"
                                       "}")
            self.widget_4.setStyleSheet("QFrame{\n"
                                        f"    background-color: {self.color2};\n"
                                        "    border-radius:9px;\n"
                                        "}\n"
                                        "#stackedWidget{\n"
                                        "    background-color:transparent;\n"
                                        "}\n"
                                        "QPushButton{\n"
                                        "    border-radius:8px;\n"
                                        f"    background-color: {self.color4};\n"
                                        f"    color:{self.colortext}\n"
                                        "}\n"
                                        "QHeaderView::section::horizontal  {\n"
                                        "    border-top-left-radius:15px;\n"
                                        "    border-top-right-radius:15px;\n"
                                        f"    background-color: {self.color1};\n"
                                        f"    color: {self.colort};\n"
                                        "}\n"
                                        "QHeaderView  {\n"
                                        f"    background-color: {self.color1};\n"
                                        f"    color: {self.colort};\n"
                                        "font-weight:bold;"
                                        "}\n"
                                        "QTableWidget {\n"
                                        f"    background-color: {self.color4};\n"
                                        f"    color: {self.colortext};\n"
                                        "    border-bottom-left-radius: 15px;\n"
                                        "    border-bottom-right-radius: 15px;\n"
                                        f"    gridline-color: {self.color3};\n"
                                        f"    border: 1px solid {self.color3};\n"
                                        "font:12px;"
                                        "}\n"
                                        "QScrollBar:vertical {\n"
                                        "    border: none;\n"
                                        f"    background-color: #F0F0F0;\n"
                                        "    width: 8px;  \n"
                                        "    margin: 0px 0px 0px 0px;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical {\n"
                                        "    background-color: #C0C0C0;\n"
                                        "    min-height: 20px;\n"
                                        "    border-radius: 4px; \n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:hover {\n"
                                        "    background-color: #A0A0A0;\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
                                        "    border: none;\n"
                                        "    background: none;\n"
                                        "}\n"
                                        "QScrollBar:horizontal {\n"
                                        "    border: none;\n"
                                        "    background-color: #F0F0F0;\n"
                                        "    height: 8px;  /* Thinner scrollbar */\n"
                                        "    margin: 0px 0px 0px 0px;\n"
                                        "    }\n"
                                        "QScrollBar::handle:horizontal {\n"
                                        "    background-color: #C0C0C0;\n"
                                        "    min-width: 20px;\n"
                                        "    border-radius: 4px;  /* Adjusted for thinner scrollbar */\n"
                                        "}\n"
                                        "QScrollBar::handle:horizontal:hover {\n"
                                        "    background-color: #A0A0A0;\n"
                                        "}\n"
                                        "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
                                        "    border: none;\n"
                                        "    background: none;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{\n"
                                        "    background-color: rgb(134, 193, 199);\n"
                                        "}\n"
                                        "#page,#page_2,#page_3,#page_4{\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "QLabel,QLineEdit,QTextEdit{\n"
                                        "    background-color: transparent;\n"
                                        "    border-radius:9px;\n"
                                        "    padding-left:10px;\n"
                                        "    padding-right:10px;\n"
                                        f"    color: {self.colortext};"
                                        "}\n"
                                        f"""QRadioButton{{color: {self.colortext};}}"""
                                        "#line{\n"
                                        f"    background-color: {self.color1};\n"
                                        "    margin-left:20px;\n"
                                        "    margin-right:20px;\n"
                                        "}"
                                        """QTableWidget::item:selected {background-color: rgb(134, 193, 199);}"""
                                        "QComboBox{\n"
                                        "    padding-left:10px;\n"
                                        f"    background-color: {self.color4};"
                                        f"   border:1px solid {self.color4};"
                                        "border-radius:9px;"
                                        f"color:{self.colortext};\n"
                                        "}\n"
                                        "QComboBox::drop-down {\n"
                                        f"    background-color: transparent;\n"
                                        "    border-top-right-radius:8px;\n"
                                        "    border-bottom-right-radius:8px;\n"
                                        f"    border-left:1px solid {self.color2};\n"
                                        "}\n"
                                        f"""QComboBox QAbstractItemView {{
                                        background-color: {self.color4}; \n
                                        color: {self.colortext}; \n
                                        selection-background-color: rgb(134, 193, 199);}}"""
                                        f"""QRadioButton::indicator::unchecked {{
                                        background-color: {self.color2};
                                        border :1px solid{self.color1};
                                        border-radius:5px;
                                        }}"""

                                        )
            self.searchlineedit.setStyleSheet(f"    border-bottom:1px solid {self.color4};\n")
            self.chart.setBackgroundBrush(QColor(self.color2))
            self.chart.setTitleBrush(QColor(self.colortext))
            self.chart.setPlotAreaBackgroundBrush(QColor(self.colortext))
            self.tooltip_label.setStyleSheet(f"    background-color: {self.color5};\n"
                                        "    border-radius:9px;\n"
                                        "    padding:10px;\n"
                                        f"    color: {self.colortext};"
                                        )
            for i in self.slices:i.setBorderColor(QColor(self.color2))

            self.barchart.setPlotAreaBackgroundBrush(QColor(self.colortext))
            self.barchart.setBackgroundPen(QColor(self.color2))
            self.barchart.setBackgroundBrush(QColor(self.color2))
            self.barchart.setTitleBrush(QColor(self.colortext))
            self.bar_axisX.setLabelsBrush(QColor(self.colortext))
            self.bar_axisY1.setLabelsBrush(QColor(self.colortext))
            for bar_set in self.barseries.barSets():
                bar_set.setBorderColor(QColor(self.color2))

    def updateicons(self):

        icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'main-menu.png'))
        self.menubutton2.setIcon(icon)
        self.pushButton_8.setIcon(icon)
        self.menubutton2.setIconSize(QSize(22, 22))
        self.pushButton_8.setIconSize(QSize(40,40))
        icon1 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'home.png'))
        self.homebutton.setIcon(icon1)
        self.homebutton.setIconSize(QSize(20, 20))
        icon2 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'bin.png'))
        icon2rec = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'recycle-bin.png'))
        self.trashbutton.setIcon(icon2rec)
        self.trashbutton.setIconSize(QSize(20, 20))
        icon3 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'question.png'))
        self.helpbutton.setIcon(icon3)
        self.helpbutton.setIconSize(QSize(20, 20))
        icon4 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'cogwheel.png'))
        self.settingbutton.setIcon(icon4)
        self.settingbutton.setIconSize(QSize(20, 20))
        icon7 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'cross.png'))
        self.closesettingbutton.setIcon(icon7)
        icon8 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'excel.png'))
        icon82 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'copy.png'))
        self.createdbcopybutton.setIcon(icon82)
        self.dbtoxecxel.setIcon(icon8)
        self.pushButton_4.setIcon(icon8)
        icon5 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'save.png'))
        self.pushButton_3.setIcon(icon5)
        self.pushButton.setIcon(icon5)
        icon6 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'search.png'))
        self.searchbutton.setIcon(icon6)
        self.searchbutton.setIconSize(QSize(20, 20))
        icon7 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'plus.png'))
        self.addpersonbutton.setIcon(icon7)
        self.removepersonbutton.setIcon(icon2)
        self.adddebtbutton.setIcon(icon7)
        self.removedebtbutton.setIcon(icon2)
        self.addpersonbutton_2.setIcon(icon7)
        self.removepersonbutton_2.setIcon(icon2)
        self.adddebtbutton_2.setIcon(icon7)
        self.removedebtbutton_2.setIcon(icon2)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_92.setIcon(icon5)
        self.pushButton_10.setIcon(icon2)
        self.deletebutton.setIcon(icon2)
        self.recoverbutton.setIcon(icon5)
        self.deleteallbutton.setIcon(icon2)
        self.recoverallbutton.setIcon(icon5)
        icon8 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'excel.png'))
        self.dbtoxecxel.setIcon(icon8)
        self.dbtoxecxel.setIconSize(QSize(22, 22))
        icon10 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'statisctics.png'))
        self.pushButton_5.setIcon(icon10)
        self.pushButton_5.setIconSize(QSize(20,20))
        icon11 = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icones', self.iconepath, 'shapes.png'))
        self.pushButton_6.setIcon(icon11)
        self.pushButton_6.setIconSize(QSize(20, 20))

    def retranslateUi(self):
            _translate = QtCore.QCoreApplication.translate
            self.menubutton2.setText(_translate("mainWindow", self.lng[0][self.k]))
            self.homebutton.setText(_translate("mainWindow", self.lng[1][self.k]))
            self.trashbutton.setText(_translate("mainWindow", self.lng[2][self.k]))
            self.helpbutton.setText(_translate("mainWindow", self.lng[3][self.k]))
            self.settingbutton.setText(_translate("mainWindow", self.lng[4][self.k]))
            self.label_12.setText(_translate("mainWindow", self.lng[5][self.k]))
            self.label_13.setText(_translate("mainWindow", self.lng[6][self.k]))
            self.label_14.setText(_translate("mainWindow", self.lng[7][self.k]))
            self.label_15.setText(_translate("mainWindow", self.lng[78][self.k]))
            self.pushButton_3.setText(_translate("mainWindow", self.lng[9][self.k]))
            self.label_6.setText(_translate("mainWindow", self.lng[10][self.k]))
            self.label_2.setText(_translate("mainWindow", self.lng[11][self.k]))
            self.label_3.setText(_translate("mainWindow", self.lng[12][self.k]))
            self.label_4.setText(_translate("mainWindow", self.lng[13][self.k]))
            self.pushButton.setText(_translate("mainWindow", self.lng[9][self.k]))
            self.label_5.setText(_translate("mainWindow", self.lng[14][self.k]))
            item = self.peapoletable.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[16][self.k]))
            item = self.peapoletable.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[6][self.k]))
            item = self.peapoletable.horizontalHeaderItem(2)
            item.setText(_translate("mainWindow", self.lng[78][self.k]))
            item = self.peapoletable.horizontalHeaderItem(3)
            item.setText(_translate("mainWindow", self.lng[71][self.k]))
            item = self.peapoletable.horizontalHeaderItem(4)
            item.setText(_translate("mainWindow", self.lng[7][self.k]))
            item = self.peapoletable.horizontalHeaderItem(5)
            item.setText(_translate("mainWindow", self.lng[8][self.k]))
            item = self.peapoletable.horizontalHeaderItem(6)
            item.setText(_translate("mainWindow", self.lng[68][self.k]))
            item = self.peapoletable.horizontalHeaderItem(7)
            item.setText(_translate("mainWindow", self.lng[17][self.k]))


            self.addpersonbutton.setText(_translate("mainWindow", self.lng[18][self.k]))
            self.removepersonbutton.setText(_translate("mainWindow", self.lng[19][self.k]))
            self.label.setText(_translate("mainWindow", self.lng[20][self.k]))
            item = self.debttable.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[16][self.k]))
            item = self.debttable.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[11][self.k]))
            item = self.debttable.horizontalHeaderItem(2)
            item.setText(_translate("mainWindow", self.lng[21][self.k]))
            item = self.debttable.horizontalHeaderItem(3)
            item.setText(_translate("mainWindow", self.lng[13][self.k]))
            self.adddebtbutton.setText(_translate("mainWindow", self.lng[10][self.k]))
            self.removedebtbutton.setText(_translate("mainWindow", self.lng[22][self.k]))
            self.label_16.setText(_translate("mainWindow", self.lng[23][self.k]))
            item = self.deletedtable.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[16][self.k]))
            item = self.deletedtable.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[6][self.k]))
            item = self.deletedtable.horizontalHeaderItem(2)
            item.setText(_translate("mainWindow", self.lng[78][self.k]))
            item = self.deletedtable.horizontalHeaderItem(3)
            item.setText(_translate("mainWindow", self.lng[71][self.k]))
            item = self.deletedtable.horizontalHeaderItem(4)
            item.setText(_translate("mainWindow", self.lng[7][self.k]))
            item = self.deletedtable.horizontalHeaderItem(5)
            item.setText(_translate("mainWindow", self.lng[24][self.k]))
            item = self.deletedtable.horizontalHeaderItem(6)
            item.setText(_translate("mainWindow", self.lng[68][self.k]))
            item = self.deletedtable.horizontalHeaderItem(7)
            item.setText(_translate("mainWindow", self.lng[17][self.k]))

            self.deletebutton.setText(_translate("mainWindow", self.lng[25][self.k]))
            self.recoverbutton.setText(_translate("mainWindow", self.lng[26][self.k]))
            self.deleteallbutton.setText(_translate("mainWindow", self.lng[27][self.k]))
            self.recoverallbutton.setText(_translate("mainWindow", self.lng[28][self.k]))
            self.label_7.setText(_translate("mainWindow", self.lng[29][self.k]))

            self.closesettingbutton.setText(_translate("MainWindow", self.lng[30][self.k]))
            self.stylelabel.setText(_translate("MainWindow", self.lng[31][self.k]))
            self.stylecombobox.setItemText(0, _translate("MainWindow", self.lng[32][self.k]))
            self.stylecombobox.setItemText(1, _translate("MainWindow", self.lng[33][self.k]))
            self.stylecombobox.setItemText(2, _translate("MainWindow", self.lng[34][self.k]))
            self.iconslabel.setText(_translate("MainWindow", self.lng[35][self.k]))
            self.iconsecombobox.setItemText(0, _translate("MainWindow", self.lng[38][self.k]))
            self.iconsecombobox.setItemText(1, _translate("MainWindow", self.lng[37][self.k]))
            self.iconsecombobox.setItemText(2, _translate("MainWindow", self.lng[36][self.k]))
            self.langyagelabel.setText(_translate("MainWindow", self.lng[39][self.k]))
            self.languagecombobox.setItemText(0, _translate("MainWindow", self.lng[40][self.k]))
            self.languagecombobox.setItemText(1, _translate("MainWindow", self.lng[41][self.k]))
            self.languagecombobox.setItemText(2, _translate("MainWindow", self.lng[42][self.k]))
            self.currencylabel.setText(_translate("MainWindow", self.lng[43][self.k]))

            self.curencycombobox.setItemText(0, _translate("MainWindow", self.lng[44][self.k]))
            self.curencycombobox.setItemText(1, _translate("MainWindow", self.lng[45][self.k]))
            self.curencycombobox.setItemText(2, _translate("MainWindow", self.lng[46][self.k]))

            self.createdbcopybutton.setText(_translate("MainWindow", self.lng[47][self.k]))
            self.dbtoxecxel.setText(_translate("MainWindow", self.lng[51][self.k]))
            self.help2.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "hr { height: 1px; border-width: 0; }\n"
                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                          "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{self.lng[50][self.k]} </span><span style=\" font-size:10pt; font-weight:700;\">C:\\Users\\&quot;your user&quot;\\AppData\\Roaming\\Debt_Manager</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:700;\"><br /></p>\n"
                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{self.lng[49][self.k]} .</span></p></body></html>"))
            self.help.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{self.lng[48][self.k]} :</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; text-decoration: underline; color:#0000ff;\">amine0dev0@gmail.com</span></p></body></html>"))

            self.label_29.setText(_translate("MainWindow", self.lng[52][self.k]))
            self.label_25.setText(_translate("MainWindow", self.lng[53][self.k]))
            self.label_22.setText(_translate("MainWindow", self.lng[54][self.k]))
            self.label_23.setText(_translate("MainWindow", self.lng[55][self.k]))
            self.label_24.setText(_translate("MainWindow", self.lng[56][self.k]))
            self.pushButton_9.setText(_translate("MainWindow", self.lng[57][self.k]))
            self.pushButton_92.setText(_translate("MainWindow", self.lng[9][self.k]))
            self.pushButton_10.setText(_translate("MainWindow", self.lng[58][self.k]))
            self.pushButton_4.setText(_translate("MainWindow", self.lng[59][self.k]))
            self.pushButton_5.setText(_translate("MainWindow", self.lng[60][self.k]))
            self.pushButton_6.setText(_translate("MainWindow", self.lng[61][self.k]))

            item = self.peapoletable_2.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[16][self.k]))
            item = self.peapoletable_2.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[6][self.k]))
            item = self.peapoletable_2.horizontalHeaderItem(2)
            item.setText(_translate("mainWindow", self.lng[78][self.k]))
            item = self.peapoletable_2.horizontalHeaderItem(3)
            item.setText(_translate("mainWindow", self.lng[71][self.k]))
            item = self.peapoletable_2.horizontalHeaderItem(4)
            item.setText(_translate("mainWindow", self.lng[7][self.k]))
            item = self.peapoletable_2.horizontalHeaderItem(5)
            item.setText(_translate("mainWindow", self.lng[8][self.k]))
            item = self.peapoletable_2.horizontalHeaderItem(6)
            item.setText(_translate("mainWindow", self.lng[17][self.k]))

            item = self.debttable_2.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[16][self.k]))
            item = self.debttable_2.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[11][self.k]))
            item = self.debttable_2.horizontalHeaderItem(2)
            item.setText(_translate("mainWindow", self.lng[21][self.k]))
            item = self.debttable_2.horizontalHeaderItem(3)
            item.setText(_translate("mainWindow", self.lng[13][self.k]))

            self.addpersonbutton_2.setText(_translate("mainWindow", self.lng[18][self.k]))
            self.removepersonbutton_2.setText(_translate("mainWindow", self.lng[19][self.k]))

            self.label_32.setText(_translate("mainWindow", self.lng[20][self.k]))

            self.adddebtbutton_2.setText(_translate("mainWindow", self.lng[10][self.k]))
            self.removedebtbutton_2.setText(_translate("mainWindow", self.lng[22][self.k]))
            self.label_21.setText(_translate("mainWindow", self.lng[14][self.k]))


            item = self.tableWidget_3.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[55][self.k]))
            item = self.tableWidget_3.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[56][self.k]))

            self.label_10.setText(_translate("MainWindow", self.lng[60][self.k]))
            self.label_20.setText(_translate("MainWindow", self.lng[63][self.k]))
            #self.label_8.setText(_translate("MainWindow", self.lng[64][self.k]))
            self.label_27.setText(_translate("MainWindow", self.lng[68][self.k]))
            #self.radioButton.setText(_translate("MainWindow", self.lng[69][self.k]))
            #self.radioButton_2.setText(_translate("MainWindow", self.lng[70][self.k]))
            self.label_26.setText(_translate("MainWindow", self.lng[71][self.k]))



            item = self.tableWidget_2.horizontalHeaderItem(0)
            item.setText(_translate("mainWindow", self.lng[16][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(1)
            item.setText(_translate("mainWindow", self.lng[6][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(2)
            item.setText(_translate("mainWindow", self.lng[78][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(3)
            item.setText(_translate("mainWindow", self.lng[71][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(4)
            item.setText(_translate("mainWindow", self.lng[7][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(5)
            item.setText(_translate("mainWindow", self.lng[8][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(6)
            item.setText(_translate("mainWindow", self.lng[68][self.k]))
            item = self.tableWidget_2.horizontalHeaderItem(7)
            item.setText(_translate("mainWindow", self.lng[17][self.k]))

            self.label_9.setText(_translate("MainWindow", self.lng[72][self.k]))
            self.radioButton_3.setText(_translate("MainWindow", self.lng[73][self.k]))
            #self.radioButton_4.setText(_translate("MainWindow", self.lng[74][self.k]))
            self.radioButton_5.setText(_translate("MainWindow", self.lng[75][self.k]))
            self.checkBox.setText(_translate("MainWindow", self.lng[76][self.k]))
            self.checkBox_2.setText(_translate("MainWindow", self.lng[77][self.k]))

            self.chart.setTitle(lng[79][self.k])
            self.barchart.setTitle(lng[62][self.k])
            self.updatedashboardlabels()

    def updatedashboardlabels(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_11.setText(_translate("MainWindow", f"{self.lng[65][self.k]}\n{self.total1} {self.curencycombobox.currentText()}"))
        self.label_17.setText(_translate("MainWindow", f"{self.lng[66][self.k]}\n{self.total2}"))
        self.label_18.setText(_translate("MainWindow", f"{self.lng[67][self.k]}\n{self.total3}"))
        self.bar_axisY1.setTitleText(self.curencycombobox.currentText())