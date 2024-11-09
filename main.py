import os
import shutil
from datetime import datetime, timedelta

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow, QColorDialog, QMessageBox, QFileDialog, QHeaderView

from Debt_db import DebtDb
from Debt_uiii import Ui_mainWindow
from translate import lng2
from ipsecurety import decide
from  Dialogg import Ui_Dialog

class MainWindow(QMainWindow, Ui_mainWindow):
    animation_group = []
    db = DebtDb()
    lng2 = lng2

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateprogressBar(65, "Data")
        self.startstyle()
        self.deletaftertherty()
        self.updateprogressBar(80, "Style")
        self.peapoletable.setSortingEnabled(True)

        tables = self.findChildren(QtWidgets.QTableWidget)
        for i in tables:
            header = i.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.updateprogressBar(90, "Functions")
        #function
        self.dbtoxecxel.clicked.connect(lambda: self.dbexcel())
        self.addpersonbutton.clicked.connect(lambda: self.addPerson(0))
        self.removepersonbutton.clicked.connect(lambda: self.markremovePerson(0))
        self.pushButton_3.clicked.connect(lambda: self.editPerson())
        self.deletebutton.clicked.connect(lambda: self.delelePerson())
        self.recoverbutton.clicked.connect(lambda: self.recoverPerson())
        self.deleteallbutton.clicked.connect(lambda: self.deleleAllPerson())
        self.recoverallbutton.clicked.connect(lambda: self.recoverAllPerson())
        self.pushButton.clicked.connect(lambda: self.adddebt())
        self.removedebtbutton.clicked.connect(lambda: self.deletedebt())
        self.searchbutton.clicked.connect(lambda: self.searchfilter())

        self.addpersonbutton_2.clicked.connect(lambda: self.addPerson(1))
        self.removepersonbutton_2.clicked.connect(lambda: self.markremovePerson(1))

        #STYLE
        self.stylecombobox.currentIndexChanged.connect(lambda: self.stylechanger())
        self.languagecombobox.currentIndexChanged.connect(lambda: self.langauechanger())
        self.iconsecombobox.currentIndexChanged.connect(lambda: self.iconchanger())
        self.curencycombobox.currentIndexChanged.connect(lambda: self.curencychanger())

        self.colorlabel1.clicked.connect(lambda: self.open_color_dialog(1))
        self.colorlabel2.clicked.connect(lambda: self.open_color_dialog(2))
        self.colorlabel3.clicked.connect(lambda: self.open_color_dialog(3))
        self.colorlabel4.clicked.connect(lambda: self.open_color_dialog(4))
        self.colorlabel5.clicked.connect(lambda: self.open_color_dialog(5))
        self.colorlabel6.clicked.connect(lambda: self.open_color_dialog(6))
        self.colorlabel7.clicked.connect(lambda: self.open_color_dialog(7))

        #navigation
        self.adddebtbutton.clicked.connect(lambda: (self.openaddddebt(0)))
        self.peapoletable.itemSelectionChanged.connect(lambda :self.switchperson())
        self.peapoletable_2.itemSelectionChanged.connect(lambda :self.updatetable_2(0,0,1))
        self.tableWidget_3.itemSelectionChanged.connect(lambda:self.categorytableselected())
        self.closesettingbutton.clicked.connect(lambda: self.uianimation(self.settingswidget, 0, "Width", 150))
        self.settingbutton.clicked.connect(lambda: self.settingshelpbutton(0))
        self.helpbutton.clicked.connect(lambda: self.settingshelpbutton(2))
        self.pushButton_4.clicked.connect(lambda: self.settingshelpbutton(1))
        self.homebutton.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(0), self.updatetables(1, 1, 0)))
        self.trashbutton.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(3), self.updatetables(0, 0, 1)))
        self.pushButton_5.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(2), self.updatedashboard()))
        self.pushButton_6.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(1), self.updatetable_2(1, 1, 1)))

        self.menubutton2.clicked.connect(lambda: self.uianimation(self.widget_8, 120, "Width", 150))
        self.pushButton_8.clicked.connect(lambda: self.uianimation(self.widget_8, 120, "Width", 150))

        self.pushButton_9.clicked.connect(lambda: self.addcategory())
        self.pushButton_92.clicked.connect(lambda : self.editcategory())
        self.pushButton_10.clicked.connect(lambda : self.deletecategory())

        self.adddebtbutton_2.clicked.connect(lambda: (self.adddebt2()))
        self.removedebtbutton_2.clicked.connect(lambda: (self.deletedebt2()))
        self.createdbcopybutton.clicked.connect(lambda:self.creatDBcopy())
        self.radioButton_5.clicked.connect(lambda :self.lineEdit_5.setReadOnly(False) )
        self.radioButton_3.clicked.connect(lambda :self.lineEdit_5.setReadOnly(True) )

        self.updateprogressBar(100, "Complete")
        self.loadpage.mainwindow.close()
    def updatecharts(self):
        try:
            dbinfo = self.db.gettotalpercategory()
            data = []
            noc = ["without Category","sans catégorie","بدون فئة"]
            for value in dbinfo:
                percent = float("{:.2f}".format(float(value[1])))
                name = value[0]
                if name == "": name = noc[self.k]
                data.append([name,percent])

            self.chartt(data)
        except Exception as e:
            QMessageBox.critical(None, self.lng[4][self.k], f" {str(e)}")




    def curencychanger(self):

        self.db.savecustoms(self.stylecombobox.currentIndex(), self.iconsecombobox.currentIndex(),
                           self.languagecombobox.currentIndex(), self.curencycombobox.currentIndex())
        self.updatedashboardlabels()
    def dbexcel(self):
        try:
            save_path, _ = QFileDialog.getSaveFileName(None, "create excel copy", "Debt_Manager",
                                                       "SQLite Database Files (*.xlsx);;All Files (*)")
            if save_path:
                self.db.k = self.k
                trash = True if self.checkBox_2.isChecked() else False
                category =  True if self.checkBox.isChecked() else False
                if self.radioButton_3.isChecked():
                    type=0
                    id = ""
                    if self.db.dbtoexcel(save_path, type, id,trash,category):
                        self.creatmessagebox(self.lng2[14][self.k], self.lng2[15][self.k], "information", 0)
                #elif self.radioButton_4.isChecked():
                #    type = 1
                #    id = ""
                #    if self.db.dbtoexcel(save_path, type, id,trash,category):
                #        self.creatmessagebox(self.lng2[14][self.k], self.lng2[15][self.k], "information", 0)
                elif self.radioButton_5.isChecked():
                    type = 2
                    id = self.lineEdit_5.text()
                    if isinstance(int(id),int) and self.db.dbtoexcel(save_path, type, int(id),trash,category):
                        self.creatmessagebox(self.lng2[14][self.k], self.lng2[15][self.k], "information", 0)
                    else:
                        self.creatmessagebox(self.lng2[4][self.k], self.lng2[11][self.k], "information", 0)


        except Exception as e:
            QMessageBox.critical(None, self.lng[0][self.k], str(e))

    def creatDBcopy(self):
        try:
            appdata_path = os.getenv('APPDATA')
            db_path = os.path.join(appdata_path, 'GarageApp', 'Garage.db')
            if not os.path.exists(db_path):
                raise FileNotFoundError(f"{self.lng[19][self.k]} {db_path}")
            save_path, _ = QFileDialog.getSaveFileName(None, "Save Database Copy", "",
                                                       "SQLite Database Files (*.db);;All Files (*)")
            if save_path:
                shutil.copy2(db_path, save_path)
                QMessageBox.information(None, self.lng2[6][self.k], self.lng2[21][self.k])
            else:
                pass
        except FileNotFoundError as fnf_error:
            QMessageBox.critical(None, self.lng[4][self.k], str(fnf_error))
        except Exception as e:
            QMessageBox.critical(None, self.lng[4][self.k], f" {str(e)}")

    def searchfilter(self):
        try:
            self.updatetables(1, 0, 0)
            if self.searchlineedit.text() != "":
                rows = self.peapoletable.rowCount()
                columns = self.peapoletable.columnCount()
                content = []
                for row in range(rows):
                    for column in range(columns):
                        item = self.peapoletable.item(row, column).text()

                        if column != 7 and column != 5 and self.searchlineedit.text().lower() in item.lower():
                            content.append([self.peapoletable.item(row, 0).text(), self.peapoletable.item(row, 1).text(),
                                            self.peapoletable.item(row, 2).text(), self.peapoletable.item(row, 3).text(),
                                            self.peapoletable.item(row, 4).text(),self.peapoletable.item(row, 5).text(),self.peapoletable.item(row, 6).text(),self.peapoletable.item(row, 7).text()])

                if content:
                    self.peapoletable.clearContents()
                    self.peapoletable.clearSelection()
                    dbinfo = content
                    if dbinfo:
                        self.peapoletable.setRowCount(len(dbinfo))
                        for row, value in enumerate(dbinfo):
                            for column, item in enumerate(value):
                                if item is None: item = ""
                                table_item = QtWidgets.QTableWidgetItem(str(item))
                                table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                                self.peapoletable.setItem(row, column, table_item)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def addcategory(self):
        try:
            dialog = Ui_Dialog()
            dialog.Categoryui()
            dialog.k = self.k
            dialog.color1 = self.color1
            dialog.color2 = self.color2
            dialog.color3 = self.color3
            dialog.color4 = self.color4
            dialog.colortext = self.colortext
            dialog.colort = self.colort
            dialog.UpdateStyleSheet()
            if dialog.Dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                if dialog.description_3.text() != "":
                    if dialog.description_3.text() in self.db.getCategoryname():
                        self.creatmessagebox(self.lng2[4][self.k], self.lng2[19][self.k], "information", 0)
                    else:
                        self.db.addCategory(dialog.description_3.text(),dialog.date_3.text())
                else:self.creatmessagebox(self.lng2[4][self.k], self.lng2[16][self.k], "information", 0)
            self.updatetable_2(1, 0, 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def deletecategory(self):
        try:
            row = self.tableWidget_3.selectedItems()
            if row:
                if self.creatmessagebox(self.lng2[2][self.k], self.lng2[18][self.k], "question", 1):
                    self.db.removeCategory(row[0].text())
                    self.updatetable_2(1, 0, 0)
                    #self.db.updatecategorydeleted(row[0].text())
                    self.creatmessagebox(self.lng2[6][self.k], self.lng2[6][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def editcategory(self):
        try:
            row = self.tableWidget_3.selectedItems()
            if row:
                self.db.updateCategory(row[0].text(),self.lineEdit_4.text(),self.textEdit.toPlainText())
                self.lineEdit_4.setText("")
                self.textEdit.setText("")
                self.updatetable_2(1,0,0)
                self.creatmessagebox(self.lng2[6][self.k],self.lng2[17][self.k] , "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def categorytableselected(self):
        try:
            row = self.tableWidget_3.selectedItems()
            if row:
                self.lineEdit_4.setText(row[0].text())
                self.textEdit.setText(row[1].text())
                self.updatetable_2(0, 1, 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def deletaftertherty(self):
        try:
            dbinfo = self.db.getpersondeleted()
            if dbinfo:
                for value in dbinfo:
                    if datetime.strptime(value[5], "%Y-%m-%d") + timedelta(days=30) < datetime.today():
                        self.db.deletePersone(value[0])
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def updatetable_2(self,t1,t2,t3):
        try:
            #category table
            if t1 == 1:
                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.clearContents()
                self.tableWidget_3.clearSelection()
                self.peapoletable_2.clearContents()
                dbinfo = self.db.getCategory()

                if dbinfo:
                    self.tableWidget_3.setRowCount(len(dbinfo))
                    for row, value in enumerate(dbinfo):
                        for column, item in enumerate(value):
                            if item is None: item = ""
                            table_item = QtWidgets.QTableWidgetItem(str(item))
                            table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                            self.tableWidget_3.setItem(row, column, table_item)
            #peopol table2
            if t2 == 1:
                self.peapoletable_2.setRowCount(0)
                self.peapoletable_2.clearContents()
                self.peapoletable_2.clearSelection()
                selected = self.tableWidget_3.selectedItems()
                if selected:
                    dbinfo = self.db.getpersonBycategory(selected[0].text())
                    if dbinfo:
                        self.peapoletable_2.setRowCount(len(dbinfo))
                        for row, value in enumerate(dbinfo):
                            for column, item in enumerate(value):
                                if item is None: item = ""
                                table_item = QtWidgets.QTableWidgetItem(str(item))
                                table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                                self.peapoletable_2.setItem(row, column, table_item)
            #debt table2
            if t3 == 1:
                self.debttable_2.setRowCount(0)
                self.debttable_2.clearContents()
                self.debttable_2.clearSelection()
                selected = self.peapoletable_2.selectedItems()
                if selected:
                    dbinfo = self.db.getDebt(selected[0].text())
                    if dbinfo:
                        self.debttable_2.setRowCount(len(dbinfo))
                        for row, value in enumerate(dbinfo):
                            for column, item in enumerate(value):
                                if item is None: item = ""
                                table_item = QtWidgets.QTableWidgetItem(str(item))
                                table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                                self.debttable_2.setItem(row, column, table_item)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def updatetables(self, t1, t2, t3):
        try:
            #peapol table
            if t1 == 1:
                self.peapoletable.setRowCount(0)
                self.peapoletable.clearContents()
                self.peapoletable.clearSelection()
                self.peapoletable.sortItems(-1)

                dbinfo = self.db.getPerson()
                if dbinfo:
                    self.peapoletable.setRowCount(len(dbinfo))
                    for row, value in enumerate(dbinfo):
                        for column, item in enumerate(value):
                            if item is None: item = ""
                            table_item = QtWidgets.QTableWidgetItem(str(item))
                            table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                            self.peapoletable.setItem(row, column, table_item)
            #debttable
            if t2 == 1:
                self.debttable.setRowCount(0)
                self.debttable.clearContents()
                self.debttable.clearSelection()
                selected = self.peapoletable.selectedItems()
                if selected:
                    dbinfo = self.db.getDebt(selected[0].text())

                    if dbinfo:
                        self.debttable.setRowCount(len(dbinfo))
                        for row, value in enumerate(dbinfo):
                            for column, item in enumerate(value):
                                if item is None: item = ""
                                table_item = QtWidgets.QTableWidgetItem(str(item))
                                table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                                self.debttable.setItem(row, column, table_item)
            #trashtable
            if t3 == 1:
                self.deletaftertherty()
                self.deletedtable.setRowCount(0)
                self.deletedtable.clearContents()
                self.deletedtable.clearSelection()
                dbinfo = self.db.getpersondeleted()
                if dbinfo:
                    self.deletedtable.setRowCount(len(dbinfo))
                    for row, value in enumerate(dbinfo):
                            for column, item in enumerate(value):
                                if item is None: item = ""
                                table_item = QtWidgets.QTableWidgetItem(str(item))
                                table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                                self.deletedtable.setItem(row, column, table_item)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def updatedashboard(self):

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clearContents()
        dbinfo = self.db.getforgotten()
        if dbinfo:
            self.tableWidget_2.setRowCount(len(dbinfo))
            for row, value in enumerate(dbinfo):
                for column, item in enumerate(value):
                    if item is None: item = ""
                    table_item = QtWidgets.QTableWidgetItem(str(item))
                    table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    self.tableWidget_2.setItem(row, column, table_item)

        self.total1 = self.db.count_total()[0]
        self.total2 = self.db.count_person()[0]
        self.total3 = self.db.count_category()[0]
        self.updatedashboardlabels()
        self.updatecharts()
        self.barcharttt(self.db.gettopamountpeopol())
    def switchperson(self):
        try:
            selected = self.peapoletable.selectedItems()
            if selected:
                self.updatetables(0, 1, 0)
                self.lineEdit_7.setText(selected[1].text())
                self.lineEdit_9.setText(selected[2].text())
                self.lineEdit_10.setText(selected[3].text())
                self.lineEdit_8.setText(selected[4].text())
                self.comboBox.clear()
                for i in self.db.getCategoryname():
                    self.comboBox.addItems(i)
                self.comboBox.setCurrentText(selected[6].text())
                self.openaddddebt(1)

        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def deletedebt(self):
        try:
            selected = self.peapoletable.selectedItems()
            selecteddebt = self.debttable.selectedItems()

            if selected:
                if selecteddebt:
                    if self.creatmessagebox(self.lng2[2][self.k], self.lng2[13][self.k], "information", 1):
                        self.db.deletDebt(selecteddebt[0].text(), selected[0].text())
                        self.updatetables(0, 1, 0)
                        table_item = QtWidgets.QTableWidgetItem(str(self.db.gettotalbyid(selected[0].text())[0]))
                        table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        self.peapoletable.setItem(self.peapoletable.currentRow(), 7, table_item)
                else:
                    self.creatmessagebox(self.lng2[4][self.k], self.lng2[12][self.k], "information", 0)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def deletedebt2(self):
        try:
            selected = self.peapoletable_2.selectedItems()
            selecteddebt = self.debttable_2.selectedItems()

            if selected:
                if selecteddebt:
                    if self.creatmessagebox(self.lng2[2][self.k], self.lng2[13][self.k], "information", 1):
                        self.db.deletDebt(selecteddebt[0].text(), selected[0].text())
                        self.updatetable_2(0, 0, 1)
                        table_item = QtWidgets.QTableWidgetItem(str(self.db.gettotalbyid(selected[0].text())[0]))
                        table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        self.peapoletable_2.setItem(self.peapoletable_2.currentRow(), 6, table_item)
                else:
                    self.creatmessagebox(self.lng2[4][self.k], self.lng2[12][self.k], "information", 0)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def adddebt(self):
        try:
            selected = self.peapoletable.selectedItems()
            if selected:
                if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and isinstance(
                        float(self.lineEdit_3.text()), float):
                    self.db.adddebt(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                                    selected[0].text())
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_3.setText("")
                    self.openaddddebt(1)
                    self.updatetables(0, 1, 0)
                    table_item = QtWidgets.QTableWidgetItem(str(self.db.gettotalbyid(selected[0].text())[0]))
                    table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    self.peapoletable.setItem(self.peapoletable.currentRow(),7,table_item)
                else:
                    self.creatmessagebox(self.lng2[4][self.k], self.lng2[11][self.k], "information", 0)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def adddebt2(self):
        try:
            selected = self.peapoletable_2.selectedItems()
            if selected:
                dialog = Ui_Dialog()
                dialog.Debtui()
                dialog.k = self.k
                dialog.color1 = self.color1
                dialog.color2 = self.color2
                dialog.color3 = self.color3
                dialog.color4 = self.color4
                dialog.colortext = self.colortext
                dialog.colort = self.colort
                dialog.UpdateStyleSheet()
                dialog.date.setText(datetime.now().strftime("%Y-%m-%d %H:%M"))
                if dialog.Dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                    if dialog.description.text() != "" and dialog.date.text() != "" and isinstance(
                            float(dialog.amount.text()), float):
                        self.db.adddebt(dialog.description.text(), dialog.date.text(), dialog.amount.text(),
                                        selected[0].text())
                        self.updatetable_2(0, 0, 1)
                        table_item = QtWidgets.QTableWidgetItem(str(self.db.gettotalbyid(selected[0].text())[0]))
                        table_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        self.peapoletable_2.setItem(self.peapoletable_2.currentRow(),6,table_item)
                    else:
                        self.creatmessagebox(self.lng2[4][self.k], self.lng2[11][self.k], "information", 0)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)
    def startstyle(self):
        try:
            dbinfo = self.db.getCust()
            self.stylecombobox.setCurrentIndex(dbinfo[0][1])
            self.iconsecombobox.setCurrentIndex(dbinfo[0][2])
            self.languagecombobox.setCurrentIndex(dbinfo[0][3])
            self.curencycombobox.setCurrentIndex(dbinfo[0][4])
            self.iconchanger()
            self.langauechanger()
            self.curencychanger()
            self.updatedashboard()
            self.stylechanger()

        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def addPerson(self,type):
        try:
            dialog = Ui_Dialog()
            dialog.Personui()
            dialog.k = self.k
            dialog.color1 = self.color1
            dialog.color2 = self.color2
            dialog.color3 = self.color3
            dialog.color4 = self.color4
            dialog.colortext = self.colortext
            dialog.colort = self.colort
            dialog.UpdateStyleSheet()
            stat = True
            if type == 0:
                for i in self.db.getCategoryname():
                    dialog.comboBox.addItems(i)
                    stat = True
            elif type == 1:
                row = self.tableWidget_3.selectedItems()
                if row:
                    dialog.comboBox.addItem(row[0].text())
                    stat = True
                else:
                    stat = False
                    #dialog.Dialog.close()
                    self.creatmessagebox(self.lng2[4][self.k], self.lng2[20][self.k], "information", 0)
            if stat and dialog.Dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                if dialog.description_2.text()!="":
                    self.db.addperson(dialog.description_2.text(), dialog.date_2.text(),dialog.amount_4.text(),dialog.amount_2.text(),datetime.now().strftime("%Y-%m-%d %H:%M"),dialog.comboBox.currentText())
                    self.creatmessagebox(self.lng2[0][self.k], self.lng2[1][self.k], "information", 0)
                    if type == 0:
                        self.updatetables(1, 1, 0)
                        if self.widget_15.width() == 0:self.uianimation(self.widget_15, 500, "Width", 150)
                    elif type == 1:self.updatetable_2(0, 1, 1)
                else:self.creatmessagebox(self.lng2[4][self.k], self.lng2[16][self.k], "information", 0)

        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def markremovePerson(self,type):
        try:
            selected = None
            if type==0:selected = self.peapoletable.selectedItems()
            elif type ==1:selected = self.peapoletable_2.selectedItems()

            if selected:
                if self.creatmessagebox(self.lng2[2][self.k], self.lng2[3][self.k], "information", 1):
                    self.db.updatePersondelete(selected[0].text(), datetime.today().strftime("%Y-%m-%d"))
                    self.creatmessagebox(self.lng2[6][self.k], self.lng2[7][self.k], "information", 0)
                    if type == 0:
                        self.updatetables(1, 1, 0)
                    elif type == 1:
                        self.updatetable_2(0, 1, 1)

            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "warning", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def editPerson(self):
        try:
            selected = self.peapoletable.selectedItems()
            if selected:
                category_id = self.comboBox.currentText()
                self.db.updatePerson(selected[0].text(), self.lineEdit_7.text(), self.lineEdit_9.text(), self.lineEdit_10.text(), self.lineEdit_8.text(),category_id, datetime.now().strftime("%Y-%m-%d %H:%M"),"")
                self.lineEdit_7.setText("")
                self.lineEdit_8.setText("")
                self.lineEdit_9.setText("")
                self.lineEdit_10.setText("")

                self.updatetables(1, 0, 0)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def delelePerson(self):
        try:
            selected = self.deletedtable.selectedItems()
            if selected:
                if self.creatmessagebox(self.lng2[2][self.k], self.lng2[3][self.k], "information", 1):
                    self.db.deletePersone(selected[0].text())
                    self.updatetables(0, 0, 1)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def recoverPerson(self):
        try:
            selected = self.deletedtable.selectedItems()
            if selected:
                if self.creatmessagebox(self.lng2[2][self.k], self.lng2[8][self.k], "information", 1):
                    self.db.updatePersondelete(selected[0].text(), "")
                    self.updatetables(0, 0, 1)
            else:
                self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def deleleAllPerson(self):
        try:
            if self.creatmessagebox(self.lng2[2][self.k], self.lng2[9][self.k], "information", 1):
                self.db.deleteAllPersone()
                self.updatetables(0, 0, 1)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def recoverAllPerson(self):
        try:
            if self.creatmessagebox(self.lng2[2][self.k], self.lng2[10][self.k], "information", 1):
                self.db.recoverAllPerson()
                self.updatetables(0, 0, 1)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def langauechanger(self):
        try:
            self.k = self.languagecombobox.currentIndex()
            self.db.savecustoms(self.stylecombobox.currentIndex(), self.iconsecombobox.currentIndex(),
                                self.languagecombobox.currentIndex(), self.curencycombobox.currentIndex())
            self.retranslateUi()
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def iconchanger(self):
        try:
            self.iconepath = self.iconespath[self.iconsecombobox.currentIndex()]
            self.db.savecustoms(self.stylecombobox.currentIndex(), self.iconsecombobox.currentIndex(),
                                self.languagecombobox.currentIndex(), self.curencycombobox.currentIndex())
            self.updateicons()
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def stylechanger(self):
        try:
            if self.stylecombobox.currentIndex() == 0:
                if self.colorswidget.height() != 0: self.uianimation(self.colorswidget, 80, "Height", 150)
                self.color1 = '#191919'  # White
                self.color2 = '#FFFFFF'  # Black
                self.color3 = '#F0F0F0'  # Light Gray
                self.color4 = '#E1E1E1'  # Lighter Gray
                self.color5 = "#EEF3F5"
                self.colortext = '#000000'  # Black
                self.colort = '#FFFFFF'  # White

            self.UpdateStyleSheet()
            if self.stylecombobox.currentIndex() == 1:
                if self.colorswidget.height() != 0: self.uianimation(self.colorswidget, 80, "Height", 150)
                self.color1 = '#282828'
                self.color2 = '#191919'
                self.color3 = '#161616'
                self.color4 = '#4B4B4B'
                self.color5 = "#303537"
                self.colort = '#FFFFFF'
                self.colortext = '#FFFFFF'
                self.UpdateStyleSheet()
            if self.stylecombobox.currentIndex() == 2:
                if self.colorswidget.height() == 0: self.uianimation(self.colorswidget, 80, "Height", 150)
                dbinfo = self.db.getCust()
                self.color1 = dbinfo[0][5]
                self.color2 = dbinfo[0][6]
                self.color3 = dbinfo[0][7]
                self.color4 = dbinfo[0][8]
                self.color5 = dbinfo[0][9]
                self.colortext = dbinfo[0][10]
                self.colort = dbinfo[0][11]

            self.db.savecustoms(self.stylecombobox.currentIndex(), self.iconsecombobox.currentIndex(),
                                self.languagecombobox.currentIndex(), self.curencycombobox.currentIndex())
            self.UpdateStyleSheet()
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def openaddddebt(self, index):
        try:
            if index == 0:
                if self.peapoletable.selectedItems():
                    self.lineEdit_2.setText(datetime.now().strftime("%Y-%m-%d %H:%M"))
                    if self.frame_14.width() == 0:
                        self.uianimation(self.frame_14, 500, "Width", 150)
                        self.uianimation(self.frame_15, 0, "Width", 150)
                else:
                    self.creatmessagebox(self.lng2[4][self.k], self.lng2[5][self.k], "information", 0)

            if index == 1:
                if self.frame_14.width() != 0:
                    self.uianimation(self.frame_14, 0, "Width", 150)
                    self.uianimation(self.frame_15, 500, "Width", 150)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def open_color_dialog(self, index):
        try:
            dialog = QColorDialog()
            dialog.setOptions(QColorDialog.ColorDialogOption.ShowAlphaChannel)  # Allow alpha channel selection
            dialog.setWindowTitle("Select a Custom Color")
            color = dialog.getColor()
            if color.isValid():
                color = color.name()
                if index == 1: self.color1 = color
                if index == 2: self.color2 = color
                if index == 3: self.color3 = color
                if index == 4: self.color4 = color
                if index == 5: self.color5 = color
                if index == 6: self.colortext = color
                if index == 7: self.colort = color
                self.db.savecolors(self.color1, self.color2, self.color3, self.color4, self.color5, self.colortext, self.colort)
                self.UpdateStyleSheet()
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def creatmessagebox(self, title, text, icon, buttons):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        if icon == 'information':
            msg_box.setIcon(QMessageBox.Icon.Information)
        elif icon == 'warning':
            msg_box.setIcon(QMessageBox.Icon.Warning)
        elif icon == 'critical':
            msg_box.setIcon(QMessageBox.Icon.Critical)
        elif icon == 'question':
            msg_box.setIcon(QMessageBox.Icon.Question)
        if buttons == 1:
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        elif buttons == 2:
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.exec()
        if msg_box.clickedButton() == msg_box.button(QMessageBox.StandardButton.Ok):
            return True
        elif msg_box.clickedButton() == msg_box.button(QMessageBox.StandardButton.Cancel):
            return False
        elif msg_box.clickedButton() == msg_box.button(QMessageBox.StandardButton.Yes):
            return True
        elif msg_box.clickedButton() == msg_box.button(QMessageBox.StandardButton.No):
            return False
        return None

    def settingshelpbutton(self, index):
        try:
            if self.settingswidget.width() == 0:
                self.uianimation(self.settingswidget, 280, "Width", 150)
            elif self.settingswidget.width() > 0 and self.settingstackedwidget.currentIndex() == index:
                self.uianimation(self.settingswidget, 280, "Width", 150)
            self.settingstackedwidget.setCurrentIndex(index)
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)

    def uianimation(self, item, max, type, duration):
        try:
            size = item.width() if type == "Width" else item.height()
            maxsize = 0
            if size > 0:
                maxsize = 0
            else:
                maxsize = max
            animation = QPropertyAnimation(item, f"maximum{type}".encode('utf-8'))
            animation.setDuration(duration)
            animation.setEndValue(maxsize)
            animation.start()
            self.animation_group.append(animation)
            animation.finished.connect(lambda: self.animation_group.remove(animation))
        except Exception as e:
            self.creatmessagebox(self.lng2[4][self.k], str(e), "information", 0)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    if decide():
        window = MainWindow()
        window.show()
        app.exec()
    else:
        QMessageBox.critical(None, "Cannot Run",
                             "please buy the application before trying to run it or contact me onn aminelallati03@gmail.com")
        app.exit()
