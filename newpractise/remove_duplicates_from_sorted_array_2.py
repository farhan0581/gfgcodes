'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.


HERE 2 duplicates are allowed

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        m = {}
        ind = 0

        # sab se bada khel yaheeh hai ki hamein 2 pointers lene hain
        # agar kisi element ka count 2 ya us se kam hai, phir to dono
        # ko aage badha do , because wo to valid array hogi
        # warna pichle index ko waheen rehne do, kyun ki wahan replace ho jayega


        for i in range(len(nums)):
            m[nums[i]] = m.get(nums[i], 0)+1
            
            if m[nums[i]] <= 2:
                nums[ind] = nums[i]
                ind += 1

        return ind
        