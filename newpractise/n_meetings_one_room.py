'''
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i])
 where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only
 one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

We will sort end time in asc order and check

'''
class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        end = [i for i in sorted(enumerate(end), key=lambda x:x[1])]
        max_meet = 0
        prev_end = -9999
        print(end)
        
        for i in range(0, n):
            ind = end[i][0]
            if start[ind] > prev_end:
                max_meet += 1
                prev_end = end[i][1]
        return max_meet

    

n = 6
start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]

print(Solution().maximumMeetings(n,start,end))