class Solution:
    def rob(self, nums: List[int]) -> int:
        # there are two distinct paths: 0 ... n - 1
        # 1 ... n 
        # if we hit an edge case that involves the first or last house, this ensures we don't account for the "circilng"

        if len(nums) < 3:
            return max(nums)

        one, two = 0, 0
        for i in range(len(nums) - 1):
            tmp = max(nums[i] + one, two)
            one = two
            two = tmp
        
        first_pass = two

        one, two = 0, 0
        for i in range(1, len(nums)):
            tmp = max(nums[i] + one, two)
            one = two
            two = tmp
        
        second_pass = two
        return max(first_pass, second_pass)