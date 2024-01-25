class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        adj = [[]]*n
        indegrees = [0]*n
        print(indegrees)
    
        for item in prerequisites:
            val,ind = item[0], item[1]
            tmp = adj[ind]
            tmp.append(val)
            adj[ind] = tmp

            x = indegrees[val]
            x += 1
            indegrees[val] = x
        
        q = []
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
        

        safe = []
        while len(q) > 0:
            node = q.pop(0)
            safe.append(node)

            for adjNode in adj[node]:
                x = indegrees[adjNode]
                x -= 1
                indegrees[adjNode] = x
                if x == 0:
                    q.append(adjNode)
        
        return safe


l = [[1, 0],
    [2, 0],
    [3, 1],
    [3, 2]]
n=4
m = len(l)
print(Solution().findOrder(n,m,l))

