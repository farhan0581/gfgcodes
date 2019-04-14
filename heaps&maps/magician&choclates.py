class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def heapify(self, arr, i):
        left = 2*i + 1
        right = 2*i + 2

        largest = i

        if left < len(arr) and arr[left] > arr[largest]:
            largest = left
        
        if right < len(arr) and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            temp = arr[largest]
            arr[largest] = arr[i]
            arr[i] = temp
            self.heapify(arr, largest)


    def build_heap(self, arr):
        index = (len(arr)-1)//2

        while index >= 0:
            self.heapify(arr, index)
            index -= 1
        
        return arr

    def get_max(self, arr):
        m = arr[0]
        arr[0] = arr[0]//2
        self.heapify(arr, 0)
        return m


    def nchoc(self, k, arr):
        modulo = pow(10,9)+7
        total = 0
        self.build_heap(arr)
        print(arr)
        while k:
            _m = self.get_max(arr)
            print(arr)
            total += _m % modulo
            k -= 1
        return total


print(Solution().nchoc(11,[ 18, 90, 18, 15, 94, 60, 45, 39, 38, 77, 56, 70, 67, 91, 85, 90, 44, 26, 40, 10, 63, 36, 60, 10, 30, 47, 76, 11, 69, 38, 51, 38, 79, 68, 5, 72, 80, 49, 63 ]))