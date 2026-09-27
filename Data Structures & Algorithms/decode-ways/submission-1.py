class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        # 1 2

        def dfs(i):
            # base case: hit an index already cached
            if i in dp:
                return dp[i]
            # base case: recursing on a 0 produces no valid decodings
            if s[i] == '0':
                return 0
            
            # add the number of decodings when we take one element
            ret = dfs(i+1)
            # check if we can construct a 2 digit element 
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) >= 0 and int(s[i+1]) <= 6)):
                # add the number of decodings when we take two elements
                ret += dfs(i+2)
            
            # cache the result
            dp[i] = ret
            return dp[i]
        
        return dfs(0)



# 1 0 1 2
# 