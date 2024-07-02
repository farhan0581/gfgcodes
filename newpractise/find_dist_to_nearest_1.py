'''
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column 
number of the current cell, and i2, j2 are the row number and column number of the nearest cell having 
value 1. There should be atleast one 1 in the grid.

In this question only BFS will work and that too we have to start with the 1's (bfs queue has all 1's first)
bfs is level based traversal, so every neighbour close to 1 will be touched first, thereby 
insuring it has minimum distance from 1
'''
# /Users/farhankhan/Desktop/gfgcodes/data/min_dist_1.png
class Solution:

	#Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		m = len(grid)
		n = len(grid[0])
		vis = [[0 for i in range(n)] for i in range(m)]
		dist = [[9999999 for i in range(n)] for i in range(m)]
		q = []
		for i in range(m):
			for j in range(n):
				# start with 1s only
				if grid[i][j] == 1:
					q.append([i,j,0])
					vis[i][j] = 1
					# self.bfs(grid,vis,dist,i,j)
		
		while len(q) > 0:
			i,j,d = q.pop(0)
			
			dist[i][j] = d

			if i + 1 < m:
				if vis[i+1][j] == 0:
					q.append([i+1,j,d+1])
					# important to mark as visited
					vis[i+1][j] = 1
			if i -1 >= 0:
				if vis[i-1][j] == 0:
					q.append([i-1,j,d+1])
					vis[i-1][j] = 1
				
			if j + 1 < n:
				if vis[i][j+1] == 0:
					q.append([i,j+1,d+1])
					vis[i][j+1] = 1
				
			if j - 1 >= 0:
				if vis[i][j-1] == 0:
					q.append([i,j-1,d+1])
					vis[i][j-1] = 1
				



		print(dist)

	# this approach did not work
	'''
	def bfs(self, arr, vis, dis, i, j):
		m = len(arr)
		n = len(arr[0])

		vis[i][j] = 1
		q = []
		q.append([i,j])

		while len(q) > 0:
			i,j = q.pop(0)
			vis[i][j] = 1
			d = []
			if i + 1 < m:
				if vis[i+1][j] == 0:
					q.append([i+1,j])
					vis[i+1][j] = 1
				d.append(dis[i+1][j])
			if i -1 >= 0:
				if vis[i-1][j] == 0:
					q.append([i-1,j])
					vis[i-1][j] = 1
				d.append(dis[i-1][j])
			if j + 1 < n:
				print(j,n)
				if vis[i][j+1] == 0:
					q.append([i,j+1])
					vis[i][j+1] = 1
				d.append(dis[i][j+1])
			if j - 1 >= 0:
				if vis[i][j-1] == 0:
					q.append([i,j-1])
					vis[i][j-1] = 1
				d.append(dis[i][j-1])
			

			if arr[i][j] == 1:
				dis[i][j] = 0
			else:
				dis[i][j] = min(d) + 1
		'''
			
		


# l = [[1,0,1],[1,1,0],[1,0,0]]
l = [[0,1,1,0],[1,1,0,0],[0,0,1,1]]
Solution().nearest(l)