# Singleton/SingletonPattern.py
import datetime


class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

# x = OnlyOne('sausage')
# print(x)
# y = OnlyOne('eggs')
# print(y)
# z = OnlyOne('spam')
# print(z)
# print(x)
# print(y)

class A(object):
    instance = None
    def __init__(self, arg):
        if not A.instance:
            print ('here')
            A.instance = A(arg)
        else:
            A.instance.name = arg
        self.name = arg

    def __str__(self):
        return self.name
    def __getattr__(self, name):
        return getattr(self.instance, name)

class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger


class B(object):
    # name = datetime.datetime.now().strftime("%s")
    def __init__(self, value):
        self.name = value

    def check(self):
        return B.name

# obj = B('khan')
# obj2 = B('ilma')
# print B.name
# print obj.check()
# print obj2.check()

# obj = B('fdf')


# obj = A('farhan')
# obj2 = A('khan')
# print obj

class Singleton(object):
    """docstring for Singleton"""
    _instance = None

    def __init__(self, *args, **kwargs):
        print(kwargs)
        print '----init----'
        self.name = kwargs['name']
        self.email = kwargs['email']

    def __new__(cls, *args, **kwargs):
        print '----new-----'
        if not cls._instance:
            print('here')
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        # return super(Singleton, cls).__new__(cls, *args, **kwargs)
        cls._instance.__init__(*args, **kwargs)
        return cls._instance


obj1 = Singleton(name='farhan', email='gmail')
obj2 = Singleton(name='faizan', email='yahoo')
print(obj1.__repr__)
print(obj2.__repr__)
print(vars(obj1))
print(vars(obj2))