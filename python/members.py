class ParentClass:
    def __init__(self):
        self.__x = 1 # private
        self.y = 10 # public
        self._z = 50 # protected
 
    def print(self):
        print(self.__x, self.y, self._z)

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.__x = 2
        self.y = 20
        self._z = 30
        
c = ChildClass()
c.print()
# print(c._ParentClass__x)
# ---------------------------------------------------------------------------------------- #

class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")


class B(A):
    def __new__(self):
        print("B's __new__() invoked")

    def __init__(self):
        print("B's __init__() invoked")


def main():
    b = B()
    a = A()

main()

# ---------------------------------------------------------------------------------------- #

class A:
    def __init__(self):
        self.setI(20)
        print("i from A is", self.i)

    def setI(self, i):
        self.i = 2 * i;

class B(A):
    def __init__(self):
        super().__init__()
        
    def setI(self, i):
        self.i = 3 * i;


b = B()

# ---------------------------------------------------------------------------------------- #

class A:
    def __init__(self):
        self.setI(20)

    def setI(self, i):
        self.i = 2 * i;

class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
        
    def setI(self, i):
        self.i = 3 * i;


b = B()

# ---------------------------------------------------------------------------------------- #


class Test(object):
    def __init__(self):
        self.a = 'farhan'
        print('__init__ called')
    
    def __new__(cls):
        print('new called')
        return super().__new__(cls)

x = Test()