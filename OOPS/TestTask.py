import pyodbc
from OOPS.QueryDictionary import QueryDictionary
class StoreEmpDetails:

    def __init__(self):


        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-TH0T2G2V\SQLEXPRESS;'
                              'Database=emp_details;'
                              'Trusted_Connection=yes;')

        self.cursor = self.conn.cursor()



    def addDetails(self,name,place,salaray):
        print("write a logic to insert data into a database")
        self.cursor.execute(QueryDictionary.ADD_CUSTOMER_DETAILS.format(name=name,place=place,salary=salaray))
        self.cursor.commit()



    def getEmpdataByID(self,id):
        print("Get deatails by id")
        # return a json object

    def getEmpdataByName(self,id):
        print("Get deatails by name")
        #return a json object

    def getEmpdataByPlace(self,id):
        print("Get deatails by name")
        #return a jsonobject


obj=StoreEmpDetails()
obj.addDetails("Venkat","Canada",452145)

