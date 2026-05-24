class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen_chars = set() 
        l = 0

        for r in range(len(s)):
            # check if we can add the new char
            if s[r] not in seen_chars:
                seen_chars.add(s[r])
                max_len = max(max_len, (r - l + 1))
                continue
            
            while s[r] in seen_chars: 
                seen_chars.remove(s[l])
                l += 1
            
            seen_chars.add(s[r])
        
        return max_len