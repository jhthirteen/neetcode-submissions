class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen_chars = set()
        max_substr = 0

        for r in range(len(s)):
            # move the left pointer until we can take our character 
            while s[r] in seen_chars: 
                seen_chars.remove(s[l])
                l += 1
            
            # now, we can take s[r]
            seen_chars.add(s[r])
            max_substr = max(max_substr, (r - l + 1))
        
        return max_substr