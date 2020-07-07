from OOPS_Implementation.SchoolOperations import School
from unittest import TestCase

class DEV(School,TestCase):

    def __init__(self,name,place,standard):
        super().__init__(name,place,standard)


    def addStudentToAbacus(self):

        print("Adding Student to abacus")
