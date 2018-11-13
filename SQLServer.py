import pypyodbc
from tkinter import *

root = Tk()
connection = pypyodbc.connect(driver='{SQL Server}', server='DESKTOP-7GE22QK\SQLEXPRESS', database='TravelAgency')
cursor = connection.cursor()

hotel = input('Enter hotel')

SQLQuery = ("""Select Tours.Code_Client, Tours.Code_Employee, Tours.StartDate, Tours.EndDate, Tours.Duration, Tours.Code_Vyg, TypesOfRest.Name, Tours.Code_Hotel, Hotels.Name
From Tours
Join TypesOfRest On Tours.Code_Vyg = TypesOfRest.CodeVyg
Join Hotels On Tours.Code_Hotel = Hotels.Code_Hotel
Where Hotels.Name = """ + "'" + hotel + "'")

cursor.execute(SQLQuery)

result = cursor.fetchall()

print(result)

connection.close()
