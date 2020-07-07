class Parent1():

    def add(self):
        print("I am from Parent1")


class Parent2():

    def add(self):
        print("I am from Parent2")


class child(Parent2,Parent1):

    pass


obj=child()
obj.add()