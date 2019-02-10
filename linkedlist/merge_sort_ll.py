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
    
    def split(self, node):
        fast = node
        slow = node
        list1 = node
        # base condition
        if not node.next:
            return
 
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
            else:
                break
        list2 = slow.next
        slow.next = None
        print('--------split list-------')
        iterate(list1)
        iterate(list2)
        print('-------after split--------')
        return list1, list2


    def merge_sorted_list(self, list1, list2):
        print('--------before merging----------')
        iterate(list1)
        iterate(list2)
        start = Node(-99999)
        dummy = start

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list1:
            dummy.next = list1
        
        elif list2:
            dummy.next = list2
        print('------------after merge---------')
        iterate(start.next)
        return start.next

    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, start):
        if start.next:
            list1, list2 = self.split(start)
            self.sortList(list1)
            self.sortList(list2)
        else:
            return start
        return self.merge_sorted_list(list1, list2)
            


# l = create([11,10,9,8,7,6,5,4,3,2,1])
# l = create([1])
# iterate(l)
# l.iterate()
# l.start = l.reverse_in_groups(l.start, 2)
l1 = create([5,1,2,3,6,4])
# l2 = create([13])
# iterate(l1)
# l1,l2 = Solution().split(l1)
# iterate(l1)
# iterate(l2)
# l = Solution().merge_sorted_list(l1,l2)
l = Solution().sortList(l1)
iterate(l)