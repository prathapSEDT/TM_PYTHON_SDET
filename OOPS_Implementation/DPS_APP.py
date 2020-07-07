from OOPS_Implementation.SchoolOperations import School
class DPS(School):

    skating_tracks=5
    swimmingpools=2

    def __init__(self,name,place,standard):
        super().__init__(name,place,standard)

    def addStudentToMusicClass(self):
        print("Adding student {name} to the music class ".format(name=self.name))




obj=DPS("Prathap","Hyd","xth class")

obj.addStudent()
obj.addStudentToMusicClass()