# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if new_interval.start > new_interval.end:
            temp = new_interval.start
            new_interval.start = new_interval.end
            new_interval.end = temp
        start = end = None
        if not intervals:
            return [new_interval]
        for index, item in enumerate(intervals):
            if new_interval.start > item.start and new_interval.start < item.end:
                start = index
            if new_interval.end > item.start and new_interval.end < item.end:
                end = index
        
        print(start, end)
        # print(intervals)
        if start != None and end !=None:
            new = Interval(intervals[start].start, intervals[end].end)
            del intervals[start:end+1]
            intervals.insert(start, new)
        
        elif start !=None and end == None:
            new = Interval(intervals[start].start, new_interval.end)
            intervals[start] = new
        
        elif start == None and end == None:
            flag = 0
            for index,item in enumerate(intervals):
                if new_interval.start < item.start and new_interval.end < item.start:
                    intervals.insert(index, new_interval)
                    flag = 1
                    break
            if not flag:
                if new_interval.start > intervals[-1].end and new_interval.end > intervals[-1].end:
                    intervals.append(new_interval)
                else:
                    return [new_interval]
        elif start==None and end!=None:
            new = Interval(new_interval.start, intervals[end].end)
            intervals[end]= new

        for i in intervals:
            print(i.start,i.end)

        return intervals

# print(Solution().insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)],Interval(4,9)))
# print(Solution().insert([ Interval(1, 2), Interval(8,10) ], Interval(13,16)))
print(Solution().insert([ Interval(3, 6), Interval(7,10), Interval(11,19) ], Interval(1,5)))
# print(Solution().insert([ Interval(3, 5), Interval(8,10) ], Interval(1,16)))
# print(Solution().insert([], Interval(2,5)))
