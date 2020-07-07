import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-TH0T2G2V\SQLEXPRESS;'
                      'Database=emp_details;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('select * from emp_history')

for row in cursor:
    print(row)