class Calcualtor:
    num = 100
    def __init__(self,a,b):
        print("this is constructor")
        self.a = a
        self.b = b



    def getsum(self):
        print("the value of the country depends on value")
        return self.a + self.b

obj1 = Calcualtor(100,200)
print(obj1.getsum())
