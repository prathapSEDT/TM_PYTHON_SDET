class School:
    id=1
   # any variables that were created here called as class level variables
    def __init__(self,name,place,standard):
        self.name=name #when we want to craete any variable which would be a parametrize value, you can create a class variable by using self ekyword
        self.place=place
        self.standard=standard

    def addStudent(self):

        print("Adding Student to the database : Name {name} , Place {place} , Standard {std} , ID {id}".format(name=self.name,
                                                                                                               place=self.place,
                                                                                                               std=self.standard,
                                                                                                               id=self.id
                                                                                                             ))

    def delStudent(self,id):
        print("Deleting student")#write logic to delete on database


    def getStudentDetails(self,id):
        print("Get studend details by id")# write logic to get details from DB
        