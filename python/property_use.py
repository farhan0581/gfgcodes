class ExampleOnProperty(object):
    '''
        example on property in python.
    '''
    def __init__(self, *args, **kwargs):
        self._eg = None
    
    @property
    def example(self):
        print('getting the value')
        return self._eg
        
    
    @example.setter
    def example(self, value):
        print('setting the value.')
        self._eg = value
    
    @example.deleter
    def example(self):
        print('deleting the value')
        self._eg = None


obj = ExampleOnProperty()
obj.example = 'test'
print(obj.example)
del obj.example
print(obj.example)