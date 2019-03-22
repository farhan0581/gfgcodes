class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, string, n):
        numbers = [i for i in range(1,n+1)]
        start = 0
        end = len(numbers)-1

        result = []
        if len(string) > 0:
            if string[0] == 'I':
                # num = min(numbers)
                # del numbers[num]
                num = numbers[start]
                start += 1
                result.append(num)
            else:
                # num = max(numbers)
                # del numbers[num]
                num = numbers[end]
                end -= 1
                result.append(num)
        
        i = 0

        while i < len(string)-1:
            # print(numbers)
            if (string[i] == 'I' and string[i+1] == 'D') or (string[i] == 'D' and string[i+1] == 'D'):
                # num = max(numbers)
                # del numbers[num]
                num = numbers[end]
                end -= 1 
                result.append(num)
            elif (string[i] == 'I' and string[i+1] == 'I') or (string[i] == 'D' and string[i+1] == 'I'):
                # num = min(numbers)
                # del numbers[num]
                num = numbers[start]
                start += 1
                result.append(num)
            i +=1

        result.append(numbers[start])
        return result     

print(Solution().findPerm('ID',3))
print(Solution().findPerm('DDIIDIID',9))
print(Solution().findPerm('DDII',5))