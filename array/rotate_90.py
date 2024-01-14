#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,arr, n): 
        
        for i in range(n):
            for j in range(n):
                temp = arr[j][i]
                arr[j][i] = arr[i][j]
                arr[i][j] = temp
                # arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
                
        
        for i in range(n):
            for j in range(n):
                temp = arr[n-1-j][i]
                arr[n-1-j][i] = arr[j][i]
                arr[j][i] = temp
                
        
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


arr = [[1,2,3],[4,5,6],[7,8,9]]
n = 3
# obj = Solution()
# matrix = obj.rotateby90(matrix,n)
for i in range(n):
    for j in range(n):
        if j >= i:
            arr[i][j],   arr[j][i] = arr[j][i], arr[i][j]
print(arr)


# arr[1][0], arr[0][1] = arr[0][1], arr[1][0]
# print(arr)

c = n//2
print(c)

for i in range(c):
    for j in range(n):
        # temp = arr[n-1-j][i]
        # arr[n-1-j][i] = arr[j][i]
        # arr[j][i] = temp
        arr[i][j], arr[n-1-i][j] = arr[n-1-i][j], arr[i][j]
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
print()

# } Driver Code Ends