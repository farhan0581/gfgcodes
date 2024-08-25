'''
1 2 3 4 5 => [1 2 3] [4 5] maxheap minheap
'''

import heapq as hq

class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num):
        # push to first part maxheap
        hq.heappush(self.maxheap, -num)
        # then move to minheap, second part -> this ensures, minheap minimum element is always boundary.
        hq.heappush(self.minheap, -hq.heappop(self.maxheap))
        # if lenght more, then move to first part, this ensures maxheap top element is greatest.
        if len(self.minheap) > len(self.maxheap):
            hq.heappush(self.maxheap, -hq.heappop(self.minheap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0]+self.minheap[0])/2
        else:
            return -self.maxheap[0]
        