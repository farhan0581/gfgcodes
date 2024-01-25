class Solution:
	

	def check(self, V, adj, vis, color):
		#code here
		
        
		q = [[V,1]]
		vis[V] = 1
		color[V] = 1

		while len(q) > 0:
			# print(vis, color)
			node, clr = q.pop(0)
			vis[node] = 1

			for adjNode in adj[node]:
				if vis[adjNode] == 0:
					q.append([adjNode, clr^1])
					vis[adjNode] = 1
					color[adjNode] = clr^1
				else:
					if clr == color[adjNode]:
						return False


		return True
	
	def isBipartite(self, V, adj):
		vis = [0 for i in range(V)]
		color = [None for i in range(V)]

		for vertex in range(V):
			if vis[vertex] == 0:
				vis[vertex] = 1
				if not self.check(vertex, adj, vis, color):
					return False
				
		return True
		




l=[[1], [0, 2], [1]]
# l = [[2,3],[3],[0,3],[0,1,2]]
v = len(l)
print(Solution().isBipartite(v,l))