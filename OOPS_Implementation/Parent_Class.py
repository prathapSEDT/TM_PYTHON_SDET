class Parent:

    houses=40
    cars=10
    hotels=5


    def runningHotels(self):

        print("Running Hotels")
    def runningSupermarkets(self):
        print("Running supermarket")


class Child(Parent):

    def __init__(self):
        pass

    def buyNewHouses(self):
        self.houses=self.houses+1

        print("Total number of houses : "+str(self.houses))


obj=Child()
obj.buyNewHouses()
obj.buyNewHouses()
obj.runningHotels()
obj.runningSupermarkets()



