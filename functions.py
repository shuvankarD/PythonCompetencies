
def greetMeet(name):#

    print("Servus " + name)

greetMeet("Shuvankar")

#classes

class Calculator:
    num = 100

    # Constructor

    def __init__(self,a, b):
        self.a = a
        self.b = b

        print("This is a Constructor")

    def getData(self):
        print("this is it")

    def addition(self):
        return self.a + self.b
obj = Calculator(2, 3)
obj.getData()
obj.num

print(obj.addition())


