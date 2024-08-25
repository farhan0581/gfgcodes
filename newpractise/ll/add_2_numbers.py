from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        carry = 0
        digit = 0
        
        while l1 and l2:
            digit = l1.val + l2.val + carry
            carry = digit // 10
            newnode = ListNode(digit%10)
            
            if head:
                cur.next = newnode
                cur = cur.next
            else:
                head = newnode
                cur = newnode
            
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            digit = l1.val + carry
            carry = digit // 10
            newnode = ListNode(digit%10)
            
            if head:
                cur.next = newnode
                cur = cur.next
            else:
                head = newnode
                cur = newnode
            
            l1 = l1.next
        
        while l2:
            digit = l2.val + carry
            carry = digit // 10
            newnode = ListNode(digit%10)
            
            if head:
                cur.next = newnode
                cur = cur.next
            else:
                head = newnode
                cur = newnode
            
            l2 = l2.next
        
        if carry:
            newnode = ListNode(1)
            cur.next = newnode


        
        return head