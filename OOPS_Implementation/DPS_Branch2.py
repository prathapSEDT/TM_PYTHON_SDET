from OOPS_Implementation.DPS_APP import DPS
class DPS_2(DPS):



    def __init__(self,name,place,standard):
        super().__init__(name, place, standard)


    def gettotalSwimmingPoolsinSchool(self):
        print(super().swimmingpools)



obj=DPS_2("prathap","Hyd","xii th class")
obj.gettotalSwimmingPoolsinSchool()


