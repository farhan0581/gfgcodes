class Solution:
    # http://www.zrzahid.com/k-th-permutation-sequence/
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fact(self, n):
        if n ==1 or n == 0:
            return 1
        return n*self.fact(n-1)

    def _solve(self, arr, fact, k, n):
        f_ind = n-1
        res = []
        for i in xrange(n):
            ind = k // fact
            res.append(arr[ind])
            del arr[ind]
            k = k - (fact*ind)
            if f_ind > 0:
                fact = fact / f_ind
            f_ind -= 1
        
        return res

    def getPermutation(self, n, k):
        arr = [i+1 for i in xrange(n)]
        f = self.fact(n-1)
        r = self._solve(arr, f, k-1, n)
        return ''.join([str(e) for e in r])
        # print(self.res[k-1])
    

print(Solution().getPermutation(4,24))


'''
Kth Permutation

Before reading this article further I strongly suggest to read my previous post to find rank of a permeation sequence. Basically given a permutation we compute how many permutations is possible to fix a number in a particular position of the array. Then we sum total such permutations for all positions to get the rank of the permutation. Now, in this question we are asking for the reverse question i.e. given the rank, find the permutation.

For example, n=4 and k=8, in this case we need to find 8th permutation in the permutation sequence of {1,2,3,4}. Below is all of 4! = 24 permutations in order. 8th permutation is [2, 1, 4, 3].

1. [1, 2, 3, 4]
2. [1, 2, 4, 3]
3. [1, 3, 2, 4]
4. [1, 3, 4, 2]
5. [1, 4, 2, 3]
6. [1, 4, 3, 2]
7. [2, 1, 3, 4]
8. [2, 1, 4, 3]
9. [2, 3, 1, 4]
10. [2, 3, 4, 1]
11. [2, 4, 1, 3]
12. [2, 4, 3, 1]
13. [3, 1, 2, 4]
14. [3, 1, 4, 2]
15. [3, 2, 1, 4]
16. [3, 2, 4, 1]
17. [3, 4, 1, 2]
18. [3, 4, 2, 1]
19. [4, 1, 2, 3]
20. [4, 1, 3, 2]
21. [4, 2, 1, 3]
22. [4, 2, 3, 1]
23. [4, 3, 1, 2]
24. [4, 3, 2, 1] 
A permutation stating with a number has (n-1) positions to permute the rest (n-1) numbers giving total (n-1)! permutations stating with each of the elements in lexicographic order. For example, n=4, We can see the first (4-1)! = 3! = 6 permutations fixed for permutations starting with 1. Next 6 position is fixed for permutations starting with 2 and so on. For each of 6 permutations starting with 1, the next position will be fixed with 2 for total (n-2)! = (4-2)! = 2! = 2 permutations.

That is, first (n-1)! permutations will start with 1, next (n-1)! permutations will start with 2 and so on. That is for a given k the permutation will start with the element at index k/(n-1)!. We need to have this element fixed at the first spot and shift the remaining numbers down to right of it.

For example, n=4 and {1,2,3,4}, for k=8th permutation will start with element at index 7/3! = 1 (for 0-based index we start with k=k-1). So, first element 8th permutation is 2 i.e kth = [2, x, x, x]. As we are skipping 3! permutations for the 1 element at position less than the index=1 and there could be 3! total such combination with the rest of 3 numbers in the rest of 3 positions, so we will decrement k by 3!x1 i.e. k' = 7-3!x1 = 1.

Once we know the first element now, we need to find what will be second element. Note that second element will be from rest of the (n-1) elements i.e. {1, 3, 4}.

Similarly, permutations with second position fixed with a number (along with first position already fixed) has (n-2) positions to permute the rest (n-2) numbers giving total (n-2)! permutations for each of the elements in the second position. That is for a given k the permutation will start with the element at index k'/(n-2)!.

For example, continuing our example with updated k'=1 , second element will be at index 1/(4-2)! = 1/2! = 0 of {1, 3, 4} which is 1 i.e kth = [2, 1, x, x]. As we are skipping permutations for 0 elements at position less than the index=0 with 2 elements to put in rest of 2 positions, so we will decrement k' by 2!x0 i.e. k" = 1-2!x0 = 1.

Next, with updated k"=1 , third element will be at index 1/(4-3)! = 1/1 = 1 of {3, 4} which is 4 i.e kth = [2, 1, 4, x]. As we are skipping permutations for 1 elements at position less than the index=1 with 1 elements to put in remaining 1 position, so we will decrement k by 1!x1 i.e. k"' = 1-1!x1 = 0.

Next, with updated k"'=0 , fourth element will be at index 0/(4-4)! = 0/1 = 0 of {3} which is 3 i.e kth = [2, 1, 4, 3]. As we are skipping permutations for 0 elements at position less than the index=0 with 0 elements remaining, so we will decrement k by 0!x0 i.e. k"" = 0-0!x0 = 0.

Now, we have tried all position so, we stop here and thus the resulting kth permutation is [2, 1, 4, 3].

Below is the implementation of the above idea. In order to handle the shrinking input set we used simple array shift to move the required element in the desired position and shift the rest of the element to right to maintain the order. So, overall complexity is O(n^2).
'''