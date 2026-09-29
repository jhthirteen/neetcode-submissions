class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret, tmp_min, tmp_max = nums[0], 1, 1

        for n in nums: 
            # store the initial tmp_max computation before updating
            tmp = tmp_max * n
            # n itself could be the min / max, edge case of a single value subarray
            tmp_max = max(tmp, tmp_min * n, n)
            tmp_min = min(tmp, tmp_min * n, n)
            ret = max(ret, tmp_max)
        return ret