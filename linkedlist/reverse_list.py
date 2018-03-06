class Node(object):
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

    def reverse_in_groups(self, k=3):
        current = self.start
        prev = None
        next = None
        count = 0
        
        # reversal of k nodes
        while current and count < 3:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        
        count = 0

        if self.start.next:
            self.start.next = current
        # skip k nodes
        while count < 3:
            if current:
                current = current.next
            else:
                break
            count += 1

        if current is not None:
            current.next = self.reverse_in_groups()

        return prev





l = LList()
l.create([9,8,7,6,5,4,3,2,1])
l.iterate()
# l.reverse()
# l.iterate()
l.reverse_in_groups()
l.iterate()

