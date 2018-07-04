class A(object):
    x = "dsds"
    def __init__(self, arg):
        self.arg=arg
        print('here a')
    
    def test(self):
        print('int tst')
        # print 'in __init__'

    def __call__(self, arg):
        self.arg=arg
        # print 'in __call__'
    
    @staticmethod
    def here():
        pass
        # print A.x
        # return A.x


# obj=A('obj1')
# obj('test')
# obj.test()


class B(A):
    var = 'asdf'
    """docstring for B"""
    def __init__(self, arg):
        print('here b')
        self.arg = arg

class C(B):
    pass

obj2 = C('this')
obj2.test()
# from abc import ABC, abstractmethod

# class AbsTest(ABC):
#     @abstractmethod
#     def testing(self):
#         pass

# class Test(AbsTest):
#     def testing(self):
#         print('hi')

# obj = Test()

# class Check(object):

#     def called():
#         print('parent called')

#     def ridden(self):
#         print('ridden parent')
#         self.called()


# class CheckVars(Check):
#     """docstring for CheckVars"""

#     def __init__(self):
#         self.a = 'a'
#         self.b = 'b'
#     name = 'farhan'
#     email = 'fdsg@vcxv'
#     username = 'farhan_khan'
    
#     # def ridden(self):
#     #     print ('ridden child')
#     #     self.called()

#     def called(self):
#         print('called child')

#     def test(self):
#         self.testing = 'no'
#         print (vars(self))


# obj=CheckVars()
# obj.ridden()



# class ClassAsDict(object):
#     def __setitem__(self, key, item):
#         self.__dict__[key] = item

#     def __getitem__(self, key):
#         return self.__dict__[key]

#     def __repr__(self):
#         return repr(self.__dict__)


# obj = ClassAsDict()
# obj.__setitem__('age', '12' )
# obj.name = "farhan"
# print(obj)


#   """docstring for C"""
#   def __init__(self, arg):
#       self.arg = arg

#   def test(self):
#       super(C, self).test()


# class A(object):
#   id=1000
#   def __init__(self, val):
#       self.__id=val
#       id = 100

# B('farhan').test()