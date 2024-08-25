'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]

merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


'''
# Definition for singly-linked list.
import heapq as hq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        q = []

        for i in range(len(lists)):
            if lists[i]:
                hq.heappush(q, (lists[i].val, i))

        head = ListNode(0)
        cur = head
        while q:
            val, ind = hq.heappop(q)
            ll = lists[ind]
            node = ListNode(val)
            
            cur.next = node
            cur = cur.next

            if ll.next:
                lists[ind] = ll.next
                hq.heappush(q, (ll.next.val, ind))
        
        return head.next