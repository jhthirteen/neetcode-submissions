class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, cur, cur_sum):
            nonlocal combinations
            # check for a target sum match 
            if cur_sum == target:
                combinations.append(cur.copy())
                return 
            # stop recursion when exhausted nums elements or sum is too large
            if cur_sum > target or i >= len(nums):
                return 
            
            # branch left by taking the current number and staying 
            cur.append(nums[i])
            cur_sum += nums[i]
            backtrack(i, cur, cur_sum)
            # branch right by skipping the current number and moving the index
            cur.pop()
            cur_sum -= nums[i]
            backtrack(i + 1, cur, cur_sum)
            return
        
        backtrack(0, [], 0)
        return combinations