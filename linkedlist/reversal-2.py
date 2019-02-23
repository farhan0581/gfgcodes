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


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, start, m, n):
        skip = 1
        
        prev1 = None
        
        current = start
        
        while skip < m:
            prev1 = current
            current = current.next
            skip += 1
        
        prev = None
        prev2 = current
        # print(prev2.val, prev1.val)
        while skip <= n and current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            print(skip)
            skip += 1

        prev2.next = current
        if prev1:
            prev1.next = prev
        else:
            return prev
        
        return start


# l = LList()
l = create([12,11,10,9,8,7,6,5,4,3,2,1])
l = create([5,4,3,2,1])
iterate(l)
# l.reverse()
# l.iterate()
# l.start = l.reverse_in_groups(l.start, 2)

l = Solution().reverseBetween(l, 3, 3)
iterate(l)
