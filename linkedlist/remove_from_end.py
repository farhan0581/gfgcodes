class Node:
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

def removeNthFromEnd(head, n):
    length = 0
    count = 1
    start = head
    while start:
        start = start.next
        length += 1

    pos = length - n
    start = head
    if n == 1 and length == 1:
        return 
    if pos > 0:
        while start:
            if count == pos and start.next:
                start.next = start.next.next
                break
            count += 1
            start = start.next
    else:
        if head.next:
            head = head.next
        
    return head

l = create([5,4,3,2,1])
x=removeNthFromEnd(l,5)
iterate(x)