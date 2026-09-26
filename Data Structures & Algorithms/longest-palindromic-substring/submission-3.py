class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, max_l, max_r = 0, 0, 0

        # iterate through s and simulate each index being the center of a palindrome 
        for i in range(len(s)):
            # case: odd length palindrome check 
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                # valid palindrome, check for new max
                if max_len < (r - l + 1):
                    max_len = r - l + 1
                    max_l = l
                    max_r = r
                # move pointers out
                l -= 1
                r += 1
            # case: even length palindrome check
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                # valid palindrome, check for new max
                if max_len < (r - l + 1):
                    max_len = r - l + 1
                    max_l = l
                    max_r = r
                # move pointers out
                l -= 1
                r += 1
        
        return s[max_l:max_r+1]