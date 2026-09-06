class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        one, two = 1, 2

        for i in range(n - 2):
            tmp = one
            one = two 
            two = two + tmp
        
        return two