'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, 
check whether it contains any cycle or not.
# /Users/farhankhan/Desktop/gfgcodes/data/cycle_dag.png
'''

class Solution:

    def dfs(self,node,adj,stack,vis):
        vis[node] = 1
        
        # put in the stack
        stack[node] = 1

        for n in adj[node]:
            if vis[n] == 0:
                # if some node returned true, u also return
                if self.dfs(n,adj,stack,vis):
                    return True
            # here we check, if node is visited and it belongs to same direction
            # same direction is told by , if node is present in the stack ( recursion stack )
            # 1->2->3->4->3
            # there is a cycle
            elif stack[n] == 1:
                return True
        
        # this is important
        # we need to remove them from rec stack, so that we have a sense of direction
        # so if we move in a direction and encounter node again, there is a cycle
        # otherwise there is no cycle
        # remove is liye liya becoz , yahan aane ka matlab hai k ,
        # ham backtrack kar rahe hain, is ka matlab hamara direction badal gaya hai
        stack[node] = 0
        return False

    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        vis = [0]*V
        stack = [0]*V

        for node in range(V):
            if vis[node] == 0:
                vis[node] = 1
                if self.dfs(node,adj,stack,vis):
                    return True
        return False





l = [[1],[2],[3],[3]]
print(Solution().isCyclic(4,l))