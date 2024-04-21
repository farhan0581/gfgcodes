import heapq as hq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        hq.heapify(self.minheap)

        while len(self.minheap) > k:
            hq.heappop(self.minheap)



    def add(self, val: int) -> int:
        hq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            hq.heappop(self.minheap)
        
        return self.minheap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)