# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = fast = head
        
        while n and fast:
            fast = fast.next
            n -= 1
        
        if not fast:
            head = slow.next
            return head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        
        if slow and slow.next:
            slow.next = slow.next.next

        return head

        