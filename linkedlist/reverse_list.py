class Node(object):
    """docstring for Node"""
    def __init__(self, *args, **kwargs):
        self.value = args[0]
        self.next = None


class LList(object):
    def __init__(self, *args, **kwargs):
        self.start = None


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
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.start = prev # imp logic

    def reverse_k_alternate(self):
        pass

    def reverse_in_groups(self):
        pass


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
l = LList()
l.start = node
l.iterate()
l.reverse()
l.iterate()