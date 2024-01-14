class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m1 = None
        m2 = None
        c1 = c2 = 0


        # dont no why but they are not independent conditions.

        for num in nums:
            if c1 == 0 and num != m2:
                m1 = num
                c1 = 1
            
            elif c2 == 0 and num != m1:
                m2 = num
                c2 = 1
            elif m1 == num:
                c1 += 1
            elif m2 == num:
                c2 += 1
            else:
                c1 -=1
                c2 -=1
            
            
        
        # print(c1,c2,m1,m2)
        threhold = len(nums)/3
        # print(threhold)
        result = []
        c1 = c2 = 0

        # check again manually
        for elem in nums:
            if elem == m1:
                c1 += 1
            elif elem == m2:
                c2 += 1

        if c1 > threhold:
            result.append(m1)
        
        if c2 > threhold:
            result.append(m2)

        return result

        