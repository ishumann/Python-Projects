import sqlite3 as lite
import os

class Data_management():
    """docstring for Data_managrment"""
    def __init__(self):

        global connect
        
        path, filename = os.path.split(os.path.abspath(__file__))
        new_path = path+"\\database"
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        try:
            connect = lite.connect(new_path+"\\employee.db")
            with connect:
                cursor = connect.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS Employee(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Job_Title TEXT)")
        except Exception as e:
            print(str(e))


    def insertdata(self, name, job_title):

        try:

            with connect:
                cursor = connect.cursor()
                cursor.execute("INSERT INTO Employee(Name, Job_Title ) VALUES('"+name+"', '"+job_title+"')")
                
        except Exception as e:
            print(str(e))


    def viewdata(self):
        name = []
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute("SELECT * FROM Employee")
                rows = cursor.fetchall()
                for row in rows:
                    data = str(row[0])+' - Name : '+str(row[1])+'- Job Title : '+str(row[2])
                    name.append(data)
                
            return name

        except Exception as e:
            print(str(e))


    def deletedata(self, id):
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute("DELETE FROM Employee WHERE Id = ?", [id])
        except Exception as e:
            print(str(e))


    def updatedata(self, id, name, job_title):
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute("UPDATE Employee SET Name= ?, Job_Title = ? WHERE Id = ?",[name, job_title, id] )
        except Exception as e:
            print(str(e))

    def fetchdata(self, id):
        data = []
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute("SELECT * FROM Employee WHERE id = ?", [id])
                rows = cursor.fetchall()
                for row in rows:
                    data.append(list(row[1:]))
            return data
        except Exception as e:
            print('Exception in fetching the values :',str(e))

# data = Data_management()
# data.insert("jfhb",'sdadfdffdsfb')
# print(data.viewdata())
# print(data.fetchdata(14))
# # data.deletedata(10)
# # data.importdb()