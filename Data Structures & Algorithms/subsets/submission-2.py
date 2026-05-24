class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []

        def backtrack(i, cur):
            nonlocal subsets
            # capture appending our list after finishing recursion
            if i == len(nums):
                subsets.append(cur.copy())
                return
            
            # simulate NOT taking the current number
            backtrack(i + 1, cur)

            # simulate taking the current number
            cur.append(nums[i])
            backtrack(i + 1, cur)
            # remove current number before next round of recursion 
            cur.pop()
            return
        
        backtrack(0, [])
        return subsets