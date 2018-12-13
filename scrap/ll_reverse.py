class Node:
    """docstring for Node"""
    def __init__(self, *args, **kwargs):
        self.value = args[0]
        self.next = None


class LList(object):
    def __init__(self, *args, **kwargs):
        self.start = None
    
    def create(self, data):
        # creates linked list in reverse order
        next = None
        for value in data:
            obj = Node(value)
            obj.next = next
            next = obj

        self.start = next


    def iterate(self):
        next = self.start
        x = ''
        while next:
            x += "%s->" % next.value
            next = next.next
        print(x)
    

    def reverse(self):
        current = self.start
        prev = None
        while current:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
        
        self.start = prev


    def recur_reverse(self, prev, cur):
        # beautiful
        if cur:
            self.recur_reverse(cur, cur.next)
            cur.next = prev
        else:
            self.start = prev
        

    
obj = LList()
obj.create([5,4,3,2,1])
obj.iterate()
obj.reverse()
obj.recur_reverse(None, obj.start)
obj.iterate()