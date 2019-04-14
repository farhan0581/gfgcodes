class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def _heapify(self, arr, i):
        left = 2*i + 1
        right = 2*i + 2

        if left >= len(arr) and right >= len(arr):
            return  
        
        largest = i

        if left < len(arr) and arr[left] > arr[largest]:
            largest = left
        
        if right < len(arr) and arr[right] > arr[largest]:
            largest = right
        
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp

        self.heapify(arr, largest)
    
    def heapify(self, arr, i):
        left = 2*i + 1
        right = 2*i + 2

        if left >= len(arr) and right >= len(arr):
            return
        
        largest = i

        if left < len(arr) and arr[left][0] >= arr[largest][0]:
            largest = left
        
        if right < len(arr) and arr[right][0] >= arr[largest][0]:
            largest = right
        
        # important base condition
        if largest != i:

            temp = arr[largest]
            arr[largest] = arr[i]
            arr[i] = temp
            self.heapify(arr, largest)
    
    def get_max(self, arr):
        maximum = arr[0]
        arr[0] = arr[-1]
        del arr[-1]
        self.heapify(arr, 0)
        return maximum, arr
    
    def correct_position(self, arr, i):
        parent = (i-1)//2
        if parent >= 0:
            if arr[parent][0] < arr[i][0]:
                temp = arr[i]
                arr[parent] = arr[i]
                arr[i] = temp
                self.correct_position(arr, parent)


    def build_heap(self, arr):
        
        index = (len(arr)-1)//2

        while index >= 0:
            self.heapify(arr, index)
            index -= 1
        return arr

    def solve(self, lis1, lis2):
        lis1 = sorted(lis1)
        lis2 = sorted(lis2)
        track = {}
        temp = []
        result = []
        i = j = len(lis1)-1
        
        count = 1
        temp.append([lis1[i]+lis2[j], i, j])
        key = "%s_%s" % (i, j)
        track[key]=1

        while count <= len(lis1):
            maximum, temp = self.get_max(temp)
            result.append(maximum[0])

            i = maximum[1]
            j = maximum[2]

            k1 = "%s_%s" % (i-1, j)
            k2 = "%s_%s" % (i, j-1)
            try:
                track[k1]
            except:
                track[k1] = 1
                temp.append([lis1[i-1]+lis2[j], i-1, j])
                self.correct_position(temp, len(temp)-1)
            try:
                track[k2]
            except:
                track[k2] = 1
                temp.append([lis1[i]+lis2[j-1], i, j-1])
                self.correct_position(temp, len(temp)-1)
            count += 1
        return result

            


print(Solution().solve([ 36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12, -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41, 30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0, 37, -42, 26, 28 ],
[ 38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2, 6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33, -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22, -9, 0, 43 ]))