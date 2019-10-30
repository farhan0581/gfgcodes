# https://www.geeksforgeeks.org/find-the-smallest-binary-digit-multiple-of-given-number/

class Solution:
    def multiple(self, n):
        mod = {}
        q = ['1']
        while q:
            # print(q)
            elem = q[0]
            del q[0]
            if int(elem) % n == 0:
                return elem
            r = int(elem) % n
            n1 = "%s0" % elem
            n2 = "%s1" % elem
            # print(n1,n2)
            # m1 = int(elem) % n
            # m2 = int(n2) % n
            try:
                mod[r]
                # if int(x) < int(elem):
                #     q.append("%s0"%x)
                # else:
                #     q.append(n1)    
            except:
                q.append(n1)
                q.append(n2)
                mod[r] = 1


print(Solution().multiple(17))
