class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # base case, if we reach the end of s return True
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            # at each index i, try to match a word to the end of the string
            for word in wordDict:
                # when we have a match, we need to check the following positions state
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                # if dp[i] ever becomes True, quit trying to match words
                if dp[i]:
                    break
        
        return dp[0]
