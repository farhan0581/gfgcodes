'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
self loop is also taken care of.


this is easy

just like topological sort using bfs
we just need to reverse the graph



'''



class Solution(object):
    def eventualSafeNodes(self,V, adj):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safe = []

        revadj = [[] for i in range(V)]
        indegrees = [0 for i in range(V)]
        q = []

        # we need to reverse the graph, then we can apply the indegrees hack
        for ind,val in enumerate(adj):
            for node in val:
                tmp = revadj[node]
                tmp.append(ind)
                revadj[node] = tmp
        
        
        for item in revadj:
            for node in item:
                indegrees[node]+=1
        
        for i in range(V):
            if indegrees[i] == 0:
                q.append(i)
        

        while len(q) > 0:
            node = q.pop(0)
            safe.append(node)

            for adjNode in revadj[node]:
                x = indegrees[adjNode]
                x -= 1
                indegrees[adjNode] = x
                if x == 0:
                    q.append(adjNode)
        
        return sorted(safe)




l = [[1,2],[2,3],[5],[0],[5],[],[]]
# l = [[1],[2],[0]]
# l = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

print(Solution().eventualSafeNodes(len(l),l))