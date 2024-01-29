'''
The problem is to find the shortest distances between every pair of vertices 
in a given edge-weighted directed graph. The graph is represented as an adjacency
 matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. 
 If Matrix[i][j]=-1, it means there is no edge from i to j.
Do it in-place.


This is used for multi source shortest distance graph
The order is n3

How to detect negative cycle in this algo ?

after we compute shortest path, if
if arr[i][j] < 0
    return True

'''
class Solution:
    def shortest_distance(self, matrix):
        #Code here
        INF = 1e8
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = INF
                if i == j:
                    matrix[i][j] = 0
        

        for k in range(row):
            for i in range(row):
                for j in range(col):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == INF:
                    matrix[i][j] = -1
        return matrix
        

        
        for i in range:
            pass

l = [[0,1,43],[1,0,6],[-1,-1,0]]
print(Solution().shortest_distance(l))