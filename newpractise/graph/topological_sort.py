'''
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.
topological sort is possible only in DAG
for that we are using bfs here
Approach:

1. Calculate first the indegrees of all the node by traversing the adjacency matric
2. After that push all the nodes whose indegrees are 0, because they must be present before in the topo sort
3. After that use simple bfs like, but decrease the indegree when you pop the node,
4. if indegree becomes 0, push it to queue.
5. continue

'''
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0 for i in range(V)]
        for item in adj:
            for node in item:
                x = indegree[node]
                x += 1
                indegree[node] = x

        q = []

        for ind,val in enumerate(indegree):
            if val == 0:
                q.append(ind)
        
        safe = []
        while len(q) > 0:
            node = q.pop(0)
            safe.append(node)

            for adjNode in adj[node]:
                x = indegree[adjNode]
                x -= 1
                if x == 0:
                    q.append(adjNode)
                indegree[adjNode] = x

        return safe    



l = [[],[0],[0],[0]]
print(Solution().topoSort(len(l),l))