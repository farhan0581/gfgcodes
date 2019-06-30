class Solution:

    def seats(self, string):
        arr = list(string)
        MOD = 10000003
        seats = []
        distance = 0
        c = 0
        _m = 0
        for i in xrange(len(arr)):
            if arr[i] == 'x':
                seats.append(i)
                c += 1
        if c % 2 == 0:
            median = (c//2 + (c-1)//2)//2
        else:
            median = c//2
        #base
        if c == 0:
            return 0
        mind = seats[median]
        # print(seats, median, mind)
        i = mind
        j = len(seats[:median])
        # print(i,j)
        while i >= 0 and j >= 0:
            if arr[i] == '.':
                distance = (distance + i-seats[j]) % MOD
                arr[i] = 'x'
                arr[seats[j]] = '.'
                j -= 1
            elif arr[i] == 'x':
                j -= 1
            i -= 1
        j = median
        # print(mind,j)
        i = mind
        while i < len(arr) and j < len(seats):
            if arr[i] == '.' and j < len(seats):
                distance = (distance + seats[j]-i) % MOD
                arr[i] = 'x'
                arr[seats[j]] = '.'
                j += 1
            elif arr[i] == 'x':
                j += 1
            i += 1
        
        return distance % MOD


        

print(Solution().seats("...."))        
print(Solution().seats("....x..xx...x.."))
print(Solution().seats("....x.x.x.x.x...."))