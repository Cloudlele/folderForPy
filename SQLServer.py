import pypyodbc
import json

connection = pypyodbc.connect(driver='{SQL Server}', server='DESKTOP-7GE22QK\SQLEXPRESS', database='TravelAgency')
cursor = connection.cursor()


SQLQuery = ("""Select Employees.PIP, Employees.Years, Employees.Phone
From Employees""")

cursor.execute(SQLQuery)
result = cursor.fetchall()
json.dumps(result)
print(result)

connection.close()
