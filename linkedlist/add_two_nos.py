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

def addTwoNumbers(n1, n2):
    sum = carry = 0
    c1 = c2 = 0
    s1 = n1
    s2 = n2
    while True:
        if n1 and n2:
            temp = n1.val + n2.val + carry
            sum = temp % 10
            carry = temp // 10
            n1.val = sum
            n2.val = sum
            prev = n1
            n1 = n1.next
            n2 = n2.next
            c1 += 1
            c2 += 1
        elif n1 and not n2:
            c1 += 1 
            temp = n1.val + carry
            sum = temp % 10
            carry = temp // 10
            n1.val = sum
            prev = n1
            n1 = n1.next            

        elif n2 and not n1:
            c2 += 1
            temp = n2.val + carry
            sum = temp % 10
            carry = temp // 10
            n2.val = sum
            prev = n2
            n2 = n2.next
        else:
            if carry > 0:
                prev.next = Node(carry)
                if c1 >= c2 :
                    return s1
                else:
                    return s2
            return s1 if c1 >= c2 else s2
        


l2 = create([1,9,9])
l1 = create([1])
x=addTwoNumbers(l1, l2)
iterate(x)