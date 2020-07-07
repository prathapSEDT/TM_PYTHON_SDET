class EmployeeDetails:
    #class level variable or attributes


    # constructor

    def __init__(self,empName,empPlace,empSalaray):

        self.empName=empName
        self.empPlace=empPlace
        self.empSalaray=empSalaray


    #behaviours
    def addDetails(self):

        # get the data from the user and insert into database
        print("************** Inserting data into a database ************************")
        print("Employee Name : {0} , Employee Place : {1} , Employee Salary : {2}".format(self.empName,self.empPlace,self.empSalaray))


obj=EmployeeDetails("Prathap","Hyderabad",89562)
obj.addDetails()
obj=EmployeeDetails("Krish","Banglore",74566)
obj.addDetails()
