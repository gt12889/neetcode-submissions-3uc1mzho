class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        length = 0
        seen = set()
        if len(s)==1:
            length+=1
        while r<len(s):
            while r < len(s) and s[r] not in seen :
                seen.add(s[r])
                r+=1
            length = max(length,r-l)
            seen.remove(s[l])
            l+=1
        return length