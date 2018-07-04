class A(object):
    x = "dsds"
    def __init__(self, arg):
        self.arg=arg
        print('here a')
    
    def test(self):
        print('int test of A')
    
class B(A):
    def test1(self):
        print('In test of B')

class C(A):
    def test2(self):
        print('In test of C')


class D(B,C):
    pass

obj = D('farhan')
obj.test()

# According to new algo search follows : D->B->C->A 
# older algo was following DFS searching : D->B->A->C
# link : https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
