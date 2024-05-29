import heapq as hq
from typing import List

'''
sorting will take nlogn
but here we buildheap for k elements => nlogk + logk(if required)

kth largest
The idea is to construct a max-heap of elements. Since the top element of the max heap is the largest element of the heap, we will remove the top K-1 elements from the heap.  The top element will be Kth's Largest element.
To get the Kth Smallest element, we will use a min-heap. After the removal of the top k-1 elements, the Kth Smallest element is top of the Priority queue.

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        # print(minheap)
        hq.heapify(minheap)
        

        for i in range(k, len(nums)):
            # print(i)
            if minheap[0] < nums[i]:
                hq.heappop(minheap)
                hq.heappush(minheap, nums[i])
                
        
        return minheap[0]



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        bucket = [0]*len(nums)
        for num in nums:
            freq = m.get(num, 0)
            m[num] = freq + 1
        
        for num,freq in m.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        
        res = []
        for item in reversed(bucket):
            if k == 0:
                return res
            if len(item) <= k:
                res.extend(item)
                k -= len(item)
            else:
                while k:
                    for elem in item:
                        res.append(elem)
                        k -= 1
                return res


            

            
        
        m = dict(sorted(m.items(), key=lambda item: item[1], reverse=True))
        # print(m.keys())
        l = list(m.keys())
        return l[:k]
                


def mergeKSortedArrays(kArrays, k:int):
    minheap = []

    for arr in kArrays:
        for num in arr:
            hq.heappush(minheap, num)
    
    hq.heapify(minheap)
    res = []

    for i in range(len(minheap)):
        res.append(minheap[0])
        hq.heappop(minheap)
    
    return res
