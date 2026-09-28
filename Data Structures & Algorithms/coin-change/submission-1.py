class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []

        for i in range(1, amount+1):
            min_coins = float('inf')
            for c in coins: 
                if c == i:
                    min_coins = min(min_coins, 1)
                elif i - c > 0:
                    rem = i - c
                    if dp[rem-1] != -1:
                        min_coins = min(min_coins, dp[rem-1] + 1)
            if min_coins != float('inf'):
                dp.append(min_coins)
            else:
                dp.append(-1)
        
        if dp:
            return dp[-1]
        return 0