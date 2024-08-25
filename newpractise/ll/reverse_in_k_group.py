# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next
        
        if not head or k > length:
            return head
        
        cur = head
        prev = None
        count = 0
        while count < k:
            count += 1
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        if temp:
            head.next = self.reverseKGroup(temp, k)
        
        return prev
        

            


        


        