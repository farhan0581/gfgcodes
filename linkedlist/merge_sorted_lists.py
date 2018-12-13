# from reverse_list import LList
class Node(object):
    """docstring for Node"""
    def __init__(self, *args, **kwargs):
        self.val = args[0]
        self.next = None

def mergeTwoLists_(list1, list2):
    if list1 and list2:
        start = list1 if list1.val <= list2.val else list2
    else:
        return list1 if list1 else list2
    
    p1 = np1 = list1
    p2 = np2 = list2
    while True:
        
        if p1.val > p2.val:
            temp = p2.next
            p2.next = p1
            p1.next = temp
            np1 = np1.next
            np2 = p1

        else:
            temp = p1.next
            p1.next = p2
            p2.next = temp
            np2 = np2.next
            # np1 = p2
        p1 = np1
        p2 = np2
        # print(np1.val, np2.val)
        if not np1 or not np2:
            return start

def mergeTwoLists(list1, list2):
    start = Node(-9999)
    dummy = start
    
    while True:
        if list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
        
        elif list1 and not list2:
            dummy.next = list1
            break
        elif list2 and not list1:
            dummy.next = list2
            break
        else:
            break
        dummy = dummy.next
    return start.next
        
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


l1 = create([20, 8])
l2 = create([15, 11, 4])
x = mergeTwoLists(l1, l2)
iterate(x)