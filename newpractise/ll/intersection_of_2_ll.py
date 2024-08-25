# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        lena = 0
        lenb = 0
        while cur:
            cur = cur.next
            lena += 1
        
        cur = headB
        while cur:
            cur = cur.next
            lenb += 1
        
        cur1 = headA
        while lena > lenb:
            cur1 = cur1.next
            lena -= 1

        cur2 = headB
        while lenb > lena:
            cur2 = cur2.next
            lenb -= 1
        
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        
        return None

        