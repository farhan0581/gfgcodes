class Node(object):
    """docstring for Node"""
    def __init__(self, *args, **kwargs):
        self.val = args[0]
        self.next = None

def create(data):
    # creates linked list in reverse order
    next = None
    for value in data:
        obj = Node(value)
        obj.next = next
        next = obj

    return next

def iterate(start):
    next = start
    x = []
    while next:
        x.append(str(next.val))
        next = next.next
    print('->'.join(x))

def deleteDuplicates(start):

    nex = None
    dummy = Node(0)
    dummy = start
    while start:
        if start.next and start.val == start.next.val:
            start.next = start.next.next
        else:
            start = start.next
    return dummy


l2 = create([3,3,3,2,1,1,1,1])
x = deleteDuplicates(l2)
iterate(x)