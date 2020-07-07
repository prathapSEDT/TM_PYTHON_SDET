class Test:
    def add(self, a, b):
        print(a + b)


class child(Test):
    def add(self,a,b):
        print(("Adding"+str(a+b)))


obj=child()
obj.add(20,30)


