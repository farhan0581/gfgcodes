'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v = numCourses
        indegree = [0 for i in range(v)]

        adj = [[] for i in range(v)]

        for edge in prerequisites:
            u,v = edge
            indegree[v] += 1
            adj[u].append(v)
        
        q = []
        for index,v in enumerate(indegree):
            if v == 0:
                q.append(index)
        
        safe = []
        while len(q) > 0:
            node = q.pop(0)
            safe.append(node)

            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
        
        if len(safe) == numCourses:
            return True
        return False


# this is part 2, here we need to print the order
        

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        v = numCourses
        indegree = [0 for i in range(v)]
        adj = [[] for i in range(v)]

        for edge in prerequisites:
            u,v = edge[1], edge[0]
            indegree[v] += 1
            adj[u].append(v)
        
        q = []
        for node,val in enumerate(indegree):
            if val == 0:
                q.append(node)
        
        safe = []
        while len(q) > 0:
            node = q.pop(0)
            safe.append(node)

            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
        # print(safe)
        if len(safe) == numCourses:
            return safe
        return []

        