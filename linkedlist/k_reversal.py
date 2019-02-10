
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

    
    def find_middle(self):
        # slow and fast pointers, increment fast by two
        # when fast is at end slow will point to middle
        slow = self.start
        fast = self.start

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            else:
                break
            slow = slow.next

        print("middle element is %s" % slow.value)



    def reverse(self):
        current = self.start
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.start = prev # imp logic

    def reverse_k_alternate(self):
        pass


    def reverse_in_groups(self, head, k):
        current = head
        prev = None
        next = None
        count = 0
        
        # reversal of k nodes
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        
        count = 0
        
        # now head points to last node of reversed part of list
        if head:
            head.next = current
        
        # skip k nodes
        while count < k-1 and current is not None:
            current = current.next
            count += 1
        
        # recursively call remaining list
        if current is not None:
            current.next = self.reverse_in_groups(current.next, k)

        return prev



class Solution:
    def reverseList(self, start, k):
        if not start:
            return
        current = start
        prev = None
        count = 1

        while current and count <= k:
            count += 1
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        start.next = self.reverseList(current, k)
        
        return prev


# l = LList()
l = create([12,11,10,9,8,7,6,5,4,3,2,1])
iterate(l)
# l.reverse()
# l.iterate()
# l.start = l.reverse_in_groups(l.start, 2)

l = Solution().reverseList(l,6)
iterate(l)
