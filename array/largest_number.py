class Solution:

    def merge(self, arr1, arr2):
        res = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        if i < len(arr1):
            res += arr1[i:]
        elif j < len(arr2):
            res += arr2[j:]
        return res
    
    def _merge(self, arr1, arr2):
        res = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            num1 = int("%s%s" % (arr1[i],arr2[j]))
            num2 = int("%s%s" % (arr2[j], arr1[i]))
            if num1 < num2:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1
        if i < len(arr1):
            res += arr1[i:]
        elif j < len(arr2):
            res += arr2[j:]
        return res

    def mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr)/2
            arr1 = self.mergesort(arr[0:mid])
            arr2 = self.mergesort(arr[mid:]) 
            return self._merge(arr1, arr2)
        else:
            return arr

    def largestNumber(self, arr):
        sorted_array = self.mergesort(arr)
        res = ''
        limit = 0
        for elem in sorted_array:
            if elem == 0:
                limit += 1
            else:
                break
        # print(sorted_array,limit)
        for item in sorted_array[limit:]:
            res += str(item)
        if res == '':
            return '0'
        return res

print(Solution().largestNumber([0,0,0,0]))