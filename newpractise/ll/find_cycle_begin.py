# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




class Solution:
    
    def checkCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return -1

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycleNode = self.checkCycle(head)
        if cycleNode == -1:
            return None
        
        fast = cycleNode
        slow = head
        c = 0
        while True:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next
            c += 1

        