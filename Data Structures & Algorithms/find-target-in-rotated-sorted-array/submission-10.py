class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the point of rotation
        rotation_num = float('inf')
        rotation_index = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < rotation_num:
                rotation_num = nums[m]
                rotation_index = m

            # if the right half of the array is sorted --> min is in left
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        
        if nums[rotation_index] == target:
            return rotation_index
        # using the rotation index to partition the input, determine the bounds to search
        l, r = 0, len(nums) - 1
        if nums[rotation_index] < target <= nums[r]:
            l = rotation_index
        else:
            r = rotation_index - 1

        print(f'{l} {r} {rotation_index}')
        # perform a normal binary search 
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return -1