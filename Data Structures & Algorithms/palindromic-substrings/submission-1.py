class Solution:
    def countSubstrings(self, s: str) -> int:
        substrs = 0
        # iterate and treat each index as a potential center of a substr
        for i in range(len(s)):
            # check for odd-length palindromes, same starting point
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                substrs += 1
                l -= 1
                r += 1
            # check for even-length palindromes, adjacent starting points
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                substrs += 1
                l -= 1
                r += 1
        return substrs