'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        cur = head
        prev = cur
        pos = 1
        
        pr = None
        cnt = 0

        l1=l2=r1=r2=None

        if left == right:
            return head
        
        while cur:

            if pos == left-1:
                l1 = cur
            
            elif pos == right+1:
                r1 = cur
            
            elif pos == left:
                l2 = cur
            
            elif pos == right:
                r2 = cur

            if pos >= left and pos <= right:
                tmp = cur.next
                cur.next = pr
                pr = cur
                cur = tmp
            
            else:
                cur = cur.next
            
            pos += 1
        
        res = head
        
        if l1 and r2:
            l1.next = r2
        else:
            res = pr
        
        if l2 and r1:
            l2.next = r1
        

        return res



        