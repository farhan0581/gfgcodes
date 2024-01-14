'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

--
imagine this as 1 d array, convert middle to i and j
using 1 based indexing in middle element

'''
class Solution(object):
    def find_index(self, pos, m, n):
        i = (pos-1)//n
        j = pos-(n*i)
        # if i < 0:
        #     i = 0
        # if j < 1:
        #     j = 1
        return i,j-1


    def searchMatrix(self, arr, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(arr)
        cols = len(arr[0])
        n = rows*cols

        start = 1
        end = n

        # print(start,end,rows, cols)

        while start <= end:
            middle = (end+start)//2
            i,j = self.find_index(middle, rows, cols)
            # print("----",middle,i,j)
            if arr[i][j] == target:
                return True
            elif arr[i][j] > target:
                end = middle-1  
            elif arr[i][j] < target:
                start = middle+1
            

        return False



# arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# arr = [[1,3]]
# print(Solution().searchMatrix(arr, 3))


myList = [2,3,5,1,77,22]
l = [i for i in sorted(enumerate(myList), key=lambda x:x[1])]
print(l)