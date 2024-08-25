'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:
https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg

Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = {}

        cur = head

        while cur:
            f = m.get(cur.val, 0)
            m[cur.val] = f+1
            cur = cur.next
        
        cur = head
        prev = None

        while cur:
            # delete
            if m[cur.val] > 1:
                
                if prev == None:
                    head = head.next
                    cur = head
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next

            
        
        return head



