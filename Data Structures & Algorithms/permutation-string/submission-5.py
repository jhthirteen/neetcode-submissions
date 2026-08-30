class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case: if s1 is longer than s2 impossible to be True
        if len(s1) > len(s2):
            return False
        # define a fixed length character count of size len(s1)
        s1_map = {}
        for char in s1:
            if char not in s1_map:
                s1_map[char] = 0
            s1_map[char] += 1
        
        # build out the first len(s1) character count of s2
        s2_map = {}
        for i in range(len(s1)):
            if s2[i] not in s2_map:
                s2_map[s2[i]] = 0
            s2_map[s2[i]] += 1
        
        if s1_map == s2_map: 
            return True
        
        # iterate through the remaining chars of s2 and adjust the counts
        l = 0
        for r in range(len(s1), len(s2)):
            left_char = s2[l]
            right_char = s2[r]
            # remove char s[l]
            s2_map[left_char] -= 1
            if s2_map[left_char] == 0:
                del s2_map[left_char]
            
            # add char s[r]
            if right_char not in s2_map:
                s2_map[right_char] = 0
            s2_map[right_char] += 1
        
            # check if the two dicts are equal --> found a permutation 
            if s1_map == s2_map:
                return True
            
            # move the left pointer 
            l += 1
        
        return False
