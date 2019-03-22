class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, arr):
        ind = len(arr)-1
        # res = []
        sum = carry = res = 0
        flag = 1
        while ind >= 0:
            if flag:
                flag = 0
                sum = arr[ind] + 1
            else:
                sum = arr[ind] + carry
            carry = sum / 10
            res = sum % 10
            arr[ind] = res
            ind -= 1

        if carry != 0:
            arr.insert(0,carry)

        limit = 0
        for elem in arr:
            if elem == 0:
                limit += 1
            else:
                break
        return arr[limit:]


print(Solution().plusOne([0,0,0,0]))