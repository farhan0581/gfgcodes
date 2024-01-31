'''
You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size k.
Note : An island means group of 1s such that they share a common side.

 

Example 1:

Input: n = 4
m = 5
k = 4
A = {{1,1},{0,1},{3,3},{3,4}}

Output: 1 1 2 2
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
 

 

Example 2:

Input: n = 4
m = 5
k = 4
A = {{0,0},{1,1},{2,2},{3,3}}

Output: 1 2 3 4
Explanation:
0.  00000
    00000
    00000
    00000
1.  10000
    00000
    00000
    00000
2.  10000
    01000
    00000
    00000
3.  10000
    01000
    00100
    00000
4.  10000
    01000
    00100
    00010


https://takeuforward.org/graph/number-of-islands-ii-online-queries-dsu-g-51/

APPROACH:
1. First treat every cell of the 2D array as a node, independent node
2. whenenver there is a 1 for a cell in the array, we also have to check for neighbours.
3. so the idea is , when we make the cell 1, we assume its independent for now and incrase the islands as +=1
4. Then we start checking for neighbours, so here when any neighbour is 1 , we do a union by size.
5. If unionbysize returns true, then its ok, if false, it means the new cell was already part of the 
   graph in which neighbouring cell is part (ultimate parent is same).

so if True:
- merging happened, decrement
if False:
- no merging happened (because they have same parent), do not do anything

if no neighbour:
- do nothing


NOTE:
never ever make the deletion in the array while reading, do something else. In this case I used an empty array to mark that.



------------------------------------------------------------------------------------------
These types of problems are considered online query problems where we need to find the result after every query.

Let’s discuss the following observations:

Observation 1: What does each operation/query mean?
In each operation/query, an index of a cell will be given and we need to add an island on that particular cell i.e. we need to place the value 1 to that particular cell.

Observation 2: Optimizing the repeating same operations
The same operations may repeat any number of times but it is meaningless to perform all of them every time. So, we will maintain a visited array that will keep track of the cells on which the operations have been already performed. If the operations repeat, by just checking the visited array we can decide not to calculate again, and instead, just take the current answer into our account. Thus we can optimize the number of operations.

Observation 3: How to connect cells to include them in the same group or consider them a single island.
Generally, a cell is represented by two parameters i.e. row and column. But to connect the cells as we have done with nodes, we need to first represent each cell with a single number. So, we will number them from 0 to n*m-1(from left to right) where n = no. of total rows and m = total no. of columns.

For example, if a 5X4 matrix is given we will number the cell in the following way:
https://takeuforward.org/wp-content/uploads/2022/12/Screenshot-2022-12-24-001924.png

Now if we want to connect cells (1,0) and (2,0), we will just perform a union of 5 and 10. The number for representing each cell can be found using the following formula:
number = (row of the current cell*total number of columns)+column of the current cell for example, for the cell (2, 0) the number is = (2*5) + 0 = 10.

Observation 4: How to count the number of islands.
For each operation, if the given cell is not visited, we will first mark the cell visited and increase the counter by 1. Now we will check all four sides of the given cell. If any other islands are found, we will connect the current cell with each of them(If not already connected) decreasing the counter value by 1. While connecting we need to check if the cells are already connected or not. For this, we will first convert the cells’ indices into numbers using the above formula and then we will check their ultimate parents. If the parents become the same, we will not connect them as well as we will not make any changes to the counter variable. Thus the number of islands will be calculated.

Approach: 
The algorithm steps are as follows:

Initial Configuration:
Visited array: This 2D array should be initialized with 0.
Counter variable: This variable will also be initialized with 0.
Answer array: After performing the algorithm, this array will store the results after performing the queries.

First, we will iterate over all the queries selecting each at a time. Now, we can get the row and the column of the cell given in that query.
Then, we will check that cell in the visited array, if the cell is previously visited or not. 
If the cell is previously visited, we will just take the current count into our account storing that count value in our answer array and we will move on to the next query.
Otherwise, we will mark the cell as visited in the visited array and increase the value of the counter variable by 1.
Now, it’s time to connect the adjacent islands properly. For that, we will check all four adjacent cells of the current cell. If any island is found, we will first check if they(the current cell and the adjacent cell that contains an island) are already connected or not using the findUPar() method.
For checking, we will first convert the indices of the current cell and the adjacent cell into the numbers using the specified formula. Then we will check their ultimate parents.
If the ultimate parents are different, we will decrease the counter value by 1 and perform the union(either unionBySize() or unionByRank()) between those two numbers that represent the cells.
Similarly, checking all four sides and making the required changes in the counter variable, we will put the counter value into our answer array.
After performing step 2 for all the queries, we will get our final answer array containing the results for all the queries.



'''
class DisJoint:
    def __init__(self, V):
        self.vertices = V
        self.parent = [i for i in range(V+1)]
        self.size = [1 for i in range(V+1)]
        self.rank = [1 for i in range(V+1)]
    
    # ultimate parent
    def ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        # call recursively and store it
        # this is called path compression 
        self.parent[node] = self.ultimate_parent(self.parent[node])
        return self.parent[node]
        
    # union by size
    def union_by_size(self, u, v):
        ultimate_parent_u = self.ultimate_parent(u)
        ultimate_parent_v = self.ultimate_parent(v)
        if ultimate_parent_u == ultimate_parent_v:
            return False
        
        if self.size[ultimate_parent_u] < self.size[ultimate_parent_v]:
            self.parent[ultimate_parent_u] = ultimate_parent_v
            self.size[ultimate_parent_v] += self.size[ultimate_parent_u]
        else:
            self.parent[ultimate_parent_v] = ultimate_parent_u
            self.size[ultimate_parent_u] += self.size[ultimate_parent_v]
        return True


class Solution:
    def numOfIslands(self, rows, cols , operators):
        V = (rows*cols)-1
        disjoint_set = DisJoint(V)
        arr = [[0 for i in range(cols)] for i in range(rows)]

        di = [1,-1,0,0]
        dj = [0,0,1,-1]
        vis = [0 for i in range(V+1)]

        islands = 0
        ans = []
        for op in operators:
            i,j = op
            node = (i*cols) + j
            if vis[node] == 1:
                ans.append(islands)
                continue
            vis[node] = 1
            
            arr[i][j] = 1
            # assume its independent for now.
            islands += 1

            
            # check for neighbours, if it belongs to same component.
            for ind in range(4):
                ni = i+di[ind]
                nj = j+dj[ind]

                if ni >= 0 and ni < len(arr) and nj >=0 and nj < len(arr[0]):
                    if arr[ni][nj] == 1:
                        adjNode = (ni*cols) + nj
                        # means we have merged 2 islands to 1 , so decrement
                        # if False, it means, they are already connected through some other means
                        # they have the same ultimate parent, so do not decrement the count here.
                        if disjoint_set.union_by_size(node, adjNode):
                            islands -= 1
            
            ans.append(islands)
            # print(ans)
        return ans
                


n = 4
m = 5
k = 4
A = [[1,1],[0,1],[3,3],[3,4]]
A = [[0,0],[1,1],[2,2],[3,3]]

print(Solution().numOfIslands(n,m,A))