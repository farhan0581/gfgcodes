class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                return True
            
            # this is the only difference, because we dont know where
            # to go if all the boundary elements are equal
            if nums[mid] == nums[start] == nums[end]:
                start += 1
                end -= 1
                continue
            
            # first half is sorted
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        
        return False