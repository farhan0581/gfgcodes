'''
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.


APPROACH:

1. is mein agar cooling time na ho , phir to simple hai, bas number_of_tasks*per_unit_time
2. problem cooling time se hai
3. ham greedy apply karte hain for tasks with high freq will be executed first
    why ? so that we can do other tasks in between
4. so put the freq in the maxheap
   pop from heap and put back in  a temp queue if freq > 0 
   when time is equal , then put it back in the heap


'''
import heapq as hq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = {}
        for i in range(len(tasks)):
            m[tasks[i]] = m.get(tasks[i], 0) + 1
        
        q = [-val for val in m.values()] # we only need the frequency
        hq.heapify(q)

        time = 0
        temp = []
        
        while q or temp:
            time += 1
            
            if q:
                freq = hq.heappop(q)
                freq += 1

                # if freq is still there, we put in the queue at time = time + cooldown
                if freq:
                    temp.append((freq, time+n))
            
            # now check if the task waiting can be put back in the queue
            if temp and temp[0][1] == time:
                x = temp.pop(0)
                hq.heappush(q, x[0])
        
        return time
