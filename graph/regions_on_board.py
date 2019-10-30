class Solution:
    def replace(self, arr, target, res):
        boundary = []
        for i in xrange(len(arr)):
            for j in xrange(len(arr[i])):
                if arr[i][j] == target:
                    arr[i][j] = res
        return arr

    def bfs(self, arr, i, j):
        q = [(i,j)]
        while q:
            ind = q[0]
            del q[0]
            i = ind[0]
            j = ind[1]
            if arr[i][j] == '-':
                arr[i][j] = 'O'

                if i+1 < len(arr):
                    q.append((i+1,j))
                if i-1 >= 0:
                    q.append((i-1,j))
                if j+1 < len(arr[0]):
                    q.append((i,j+1))
                if j-1 < len(arr[0]):
                    q.append((i,j-1))
    
    def solve(self, arr):
        arr = self.replace(arr, 'O', '-')
        i=0
        j=0
        while j < len(arr[0]):
            if arr[i][j] == '-':
                self.bfs(arr,i,j)
            j+=1

        j = j-1
        while i < len(arr):
            if arr[i][j] == '-':
                self.bfs(arr,i,j)
            i +=1
        i = i-1
        j = j-1
        
        while j >= 0:
            if arr[i][j] == '-':
                self.bfs(arr,i,j)
            j -= 1
        
        j = 0
        while i >= 0:
            if arr[i][j] == '-':
                self.bfs(arr,i,j)
            i -= 1
        
        self.replace(arr, '-', 'X')



arr = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', "O", 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', "O", 'X', 'X']
    ]

print(Solution().solve(arr))