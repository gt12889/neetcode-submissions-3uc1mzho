class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        length = 0
        seen = set()
        if len(s)==1:
            length+=1
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            r+=1
            length = max(length,r-l)
        return length