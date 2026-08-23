class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ret = float('inf')

        while l <= r: 
            m = (l + r) // 2
            if nums[m] < ret:
                ret = nums[m]

            # check if the right portion is strictly increasing 
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        
        return ret
            