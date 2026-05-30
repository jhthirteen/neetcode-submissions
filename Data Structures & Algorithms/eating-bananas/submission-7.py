class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # helper to check if rate is valid
        def can_eat(k: int):
            hours = 0
            for bananas in piles: 
                hours += math.ceil(bananas / k)
            
            return hours <= h
        
        l, r = 1, max(piles)
        min_rate = r
        while l <= r:
            m = (l + r) // 2
            if can_eat(m):
                min_rate = m
                r = m - 1
            else:
                l = m + 1
        
        return min_rate
