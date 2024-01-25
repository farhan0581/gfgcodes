'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
self loop is also taken care of.


this is tough
'''



class Solution(object):
    def dfs(self, adj, vis, state, safe, node):

        vis[node] = 1
        state[node] = 1
        # this is important
        safe[node] = False

        for adjNode in adj[node]:
            if vis[adjNode] == 0:
                vis[adjNode] = 1
                if not self.dfs(adj,vis,state,safe,adjNode):
                    safe[adjNode] = False
                    return False
                

            else:
                if state[adjNode] == state[node]:
                    safe[adjNode] = False
                    return False
        
        state[node] = 0
        safe[node] = True
        return True


    def eventualSafeNodes(self,V, adj):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        nodes = len(adj)
        vis = [0 for i in range(nodes)]
        state = [0 for i in range(nodes)]
        safe = [None for i in range(nodes)]

        for i in range(nodes):
            if vis[i] == 0:
                vis[i] = 1
                self.dfs(adj, vis,state, safe,i)

        
        res = []
        for i in range(len(safe)):
            if safe[i] == True:
                res.append(i)
        
        return res

l = [[1,2],[2,3],[5],[0],[5],[],[]]
# l = [[1],[2],[0]]
l = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

print(Solution().eventualSafeNodes(0,l))