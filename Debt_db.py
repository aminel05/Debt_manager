import os
import sqlite3
import random

import pandas as pd


class DebtDb:
    appdata_path = os.getenv('APPDATA')
    db_path = os.path.join(appdata_path, 'Debt_Manager', 'Debt.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    connection = sqlite3.connect(db_path)
    cursur = connection.cursor()
    k = 0

    def __init__(self):
        self.createTable()
        self.cursur.execute("PRAGMA foreign_keys = ON;")
        if self.getCust() == []:
            self.insertccust()
        if self.getdefcat() == []:
            self.defaultcategory()

    def gettotalpercategory(self):
        self.cursur.execute("""
        SELECT c.name, IFNULL(SUM(p.total), 0) FROM Category c LEFT JOIN Person p ON c.name = p.category AND p.deleted == ? GROUP BY c.name;""",("",))
        return self.cursur.fetchall()
    def count_total(self):
        self.cursur.execute("""SELECT SUM(total) FROM Person WHERE deleted == ?""", ("",))
        return self.cursur.fetchone()
    def count_person(self):
        self.cursur.execute("""SELECT COUNT(id) FROM Person WHERE deleted == ?""", ("",))
        return self.cursur.fetchone()
    def count_category(self):
        self.cursur.execute("""SELECT COUNT(name) FROM Category WHERE name != ?""", ("",))
        return self.cursur.fetchone()
    def gettopamountpeopol(self):
        self.cursur.execute("""SELECT name,total FROM Person WHERE deleted == ? ORDER BY total DESC LIMIT 8 """, ("",))
        return self.cursur.fetchall()
    def getforgotten(self):
        self.cursur.execute("""SELECT id,name,nickname,phone_number,card_id,last_updated,category,total FROM Person WHERE deleted == ? ORDER BY last_updated LIMIT 5 """, ("",))
        return self.cursur.fetchall()

    def getdefcat(self):
        self.cursur.execute("""SELECT * FROM Category WHERE name == ?""", ("",))
        return self.cursur.fetchall()

    def writeexceldeleted(self,writer,header_format,center_format):
        table_header1s = [["id", "name", "nickname", "phone_number", "card id","deleted in", "category", "total"],["id", "nom", "surnom","numéro_de_téléphone", "id de la carte","supprimé le","catégorie", "total"],["المعرف", "الاسم", "كنية", "رقم الهاتف","محذوفي", "معرف البطاقة","الفئة", "المجموع"]] #Header
        table_header1 = table_header1s[self.k]

        data = self.getpersondeleted()

        sheet_name =  "deleted_person_list"
        df = pd.DataFrame(data,columns=table_header1)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        worksheet1 = writer.sheets[sheet_name]
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)  # Apply header format to the first row (header)
            worksheet1.set_column(col_num, col_num, 20, center_format)

    def write_category(self,writer,header_format,center_format):
        table_header1s = [["name", "note"],
                          ["nom", "note" ],
                          ["الاسم","ملاجظة"]]  # Header
        table_header1 = table_header1s[self.k]

        data = self.getCategory()
        sheet_name = "Categories list"
        df = pd.DataFrame(data, columns=table_header1)
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        worksheet1 = writer.sheets[sheet_name]
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)  # Apply header format
            worksheet1.set_column(col_num, col_num, 20, center_format)
    def dbtoexcel(self, path,type,id,i1,i2):
        table_header0s = [["id", "name", "nickname", "phone_number", "card id",  "last_edited", "category", "total"],["id", "nom","surnom","numéro_de_téléphone", "id de la carte", "dernière modification","catégorie", "total"],["المعرف", "الاسم", "كنية", "رقم الهاتف","معرف البطاقة", "آخر تعديل","الفئة", "الإجمالي"]]  # Header

        table_header0 = table_header0s[self.k]
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        workbook = writer.book

        center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'align': 'center', 'valign': 'vcenter'})

        data = self.getPerson() if type ==1 or type ==0 else self.getPersonByid(id)
        sheet_name = "person_list"
        df = pd.DataFrame(data, columns=table_header0 )
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        worksheet1 = writer.sheets[sheet_name]
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)  # Apply header format
            worksheet1.set_column(col_num, col_num, 20, center_format)

        if type == 0 or type == 2:
            debt_headers = [["id","description","date", "amount"],["id","description", "date",  "montant"],["المعرف","الوصف", "التاريخ",  "المبلغ"]]  # Debt header
            debt_header = debt_headers[self.k]
            debt_data = []
            data = self.getPerson() if type == 0 else self.getPersonByid(id)
            for person in data:
                person_id, person_name = person[0], person[1]
                person_debt = self.getDebt(person_id)
                if type == 0:debt_data.append([f"------------ID : {person_id}------------","---------------------", f"---------{person_name}---------",  "---------------------",""])
                debt_data.append(debt_header)
                for debt in person_debt:
                    debt_data.append(debt)
                if type == 0:debt_data.append([""] * len(debt_header))
                if type == 0:debt_data.append(["--------------------------"] * len(debt_header))
                if type == 0:debt_data.append([""] * len(debt_header))
            dff = pd.DataFrame(debt_data)
            dff.to_excel(writer, sheet_name="debt_list" if type == 0 else sheet_name, header=False, index=False, startrow=0 if type == 0 else 6)
            worksheet2 = writer.sheets["debt_list" if type == 0 else sheet_name]
            worksheet2.set_column(0, len(debt_header) - 1, 20, center_format)
            for row_num, row_data in enumerate(debt_data):
                if "id" in str(row_data[0]).lower() or row_data == debt_header and type == 0 :
                    for col in range(0, 4):
                        worksheet2.write(row_num+0 if type == 0 else 5, col, row_data[col], header_format)
        if i1:self.writeexceldeleted(writer,header_format, center_format)
        if i2:self.write_category(writer,header_format, center_format)

        writer.close()
        return True
    def defaultcategory(self):
        self.cursur.execute("""INSERT INTO Category(name,note) VALUES(?,?)""", ("",""))
        self.connection.commit()
    def addCategory(self,name,note):
        self.cursur.execute("""INSERT INTO Category(name,note) VALUES(?,?)""",(name,note))
        self.connection.commit()
    def removeCategory(self,name):
        self.cursur.execute("""UPDATE Person SET category = ? WHERE category = ?""",("",name))
        self.cursur.execute("""DELETE FROM Category WHERE name = ?""", (name,))
        self.connection.commit()
    def updateCategory(self,id,name,note):
        self.cursur.execute("""UPDATE Category SET name = ?, note = ? WHERE name = ?""", (name, note, id))
        self.connection.commit()
    def getCategory(self):
        self.cursur.execute("""SELECT name,note FROM Category WHERE name != ?""",("",))
        return self.cursur.fetchall()
    def getCategoryname(self):
        self.cursur.execute("""SELECT name FROM Category""")
        return self.cursur.fetchall()
    def getpersonBycategory(self,category):
        self.cursur.execute("SELECT id,name,nickname,phone_number,card_id,last_updated,total FROM Person WHERE deleted = ? And category = ?", ("",category))
        return self.cursur.fetchall()
    def getPerson(self):
        self.cursur.execute("SELECT id,name,nickname,phone_number,card_id,last_updated,category,total FROM Person WHERE deleted = ?", ("",))
        return self.cursur.fetchall()
    def getPersonByid(self,id):
        self.cursur.execute("SELECT id,name,nickname,phone_number,card_id,last_updated,category,total FROM Person WHERE id = ?", (id,))
        return self.cursur.fetchall()
    def updatePerson(self, id, name,nickname,phone_number,card_id,category,last_updated,deleted):
        self.cursur.execute(
            "UPDATE Person SET name = ?,nickname = ?, phone_number = ?,card_id = ?, category = ?, last_updated = ?, total = COALESCE((SELECT SUM(amount) FROM Debt WHERE person_id = ?),0) , deleted = ? WHERE id = ? ",
            ( name,nickname,phone_number,card_id,category,last_updated, id, deleted, id))
        self.connection.commit()

    def updatePersondelete(self, id,deleted):
        self.cursur.execute(
            "UPDATE Person SET deleted = ? WHERE id = ? ",
            (deleted, id))
        self.connection.commit()
    def recoverAllPerson(self):
        self.cursur.execute("UPDATE Person SET deleted = ? ",
                            ("",))
        self.connection.commit()

    def deleteAllPersone(self):
        self.cursur.execute("DELETE FROM Person WHERE deleted != ?", ("",))
        self.connection.commit()

    def deletePersone(self, id):
        self.cursur.execute("DELETE FROM Person WHERE id = ?", (id,))
        self.connection.commit()

    def deletDebt(self, id, per_id):
        self.cursur.execute("DELETE FROM Debt WHERE id = ?", (id,))
        self.cursur.execute(
            "UPDATE Person SET  total = (SELECT SUM(amount) FROM Debt WHERE person_id = ?)  WHERE id = ? ",
            (per_id, per_id))

        self.connection.commit()
    def addperson(self, name,nixknME,phone_number,card_id,last_updated,category):
        self.cursur.execute("INSERT INTO Person(name,nickname,phone_number,card_id,last_updated,total,deleted,category) VALUES (?,?,?,?,?,?,?,?)",
                            (name,nixknME,phone_number,card_id,last_updated, 0, "",category))
        self.connection.commit()

    def adddebt(self, description, date, amount, id):
        self.cursur.execute("INSERT INTO Debt(description,date,amount,person_id) VALUES (?,?,?,?)",
                            (description, date, amount, id))
        self.cursur.execute(
            "UPDATE Person SET  total = (SELECT SUM(amount) FROM Debt WHERE person_id = ?)  WHERE id = ? ", (id, id))
        self.connection.commit()
    def gettotalbyid(self,id):
        self.cursur.execute(
            "SELECT total FROM Person WHERE id = ? ", (id,))
        total = self.cursur.fetchone()
        if total[0] is None:total=0
        return total
    def getpersondeleted(self):
        self.cursur.execute("SELECT id,name,nickname,phone_number,card_id,deleted,category,total FROM Person WHERE deleted != ?", ("",))
        return self.cursur.fetchall()


    def updatecategorydeleted(self,category):
        self.cursur.execute("UPDATE Person SET category = ? WHERE category = ?", ("", category))
        self.connection.commit()

    def getDebt(self, id):
        self.cursur.execute("SELECT id,description,date,amount FROM Debt where person_id = ?", (id,))
        return self.cursur.fetchall()

    def savecustoms(self, style, icon, language, currency):
        self.cursur.execute("UPDATE Cust SET style = ?, icon = ?, language = ?, currency = ? WHERE id = 1",
                            (style, icon, language, currency))
        self.connection.commit()

    def savecolors(self, color1, color2, color3, color4,color5, colortext, colorth):
        self.cursur.execute(
            "UPDATE Cust SET color1 = ?, color2 = ?, color3 = ?, color4 = ? , color5 = ? , colortext = ? , colorht = ? WHERE id = 1",
            (color1, color2, color3, color4, color5, colortext, colorth))
        self.connection.commit()

    def insertccust(self):
        self.cursur.execute(
            "INSERT INTO Cust(style, icon, language, currency,color1, color2, color3, color4, color5, colortext, colorht) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (0, 0, 1, 0, "#009889", "#ffffff", "#ffffff", "#86c1c7", "#d8f5f5", "#000000", "#000000"))
        self.connection.commit()

    def getCust(self):
        self.cursur.execute("SELECT * FROM Cust where id = 1")
        return self.cursur.fetchall()

    def createTable(self):
        self.cursur.execute("""
            CREATE TABLE IF NOT EXISTS Category(
            name TEXT PRIMARY KEY,
            note TEXT);""")
        self.cursur.execute("""
            CREATE TABLE IF NOT EXISTS Person(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                nickname TEXT,
                phone_number TEXT,
                card_id TEXT,
                category TEXT,
                total REAL,
                deleted TEXT,
                last_updated TEXT,
                FOREIGN KEY (category) REFERENCES Category(name) ON UPDATE CASCADE
            );""")
        self.cursur.execute("""CREATE TABLE IF NOT EXISTS Debt(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                date TEXT,
                amount REAL,
                person_id INTEGER,
                FOREIGN KEY (person_id) REFERENCES Person(id) ON DELETE CASCADE
            );""")
        self.cursur.execute("""CREATE TABLE IF NOT EXISTS Cust(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                style INTEGER,
                icon INTEGER,
                language INTEGER,
                currency INTEGER,
                color1 TEXT,
                color2 TEXT,
                color3 TEXT,
                color4 TEXT,
                color5 TEXT,
                colortext TEXT,
                colorht TEXT
            );""")
        self.connection.commit()
