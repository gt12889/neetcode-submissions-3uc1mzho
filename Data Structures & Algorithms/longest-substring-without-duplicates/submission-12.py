class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l,r = 0, 0
        count = 0
        dup = defaultdict(int)
        while r<=len(s)-1:
            dup[s[r]]+=1
            while dup[s[r]] >1:
                dup[s[l]]-=1
                l+=1
            if dup[s[r]] <=1:
                r+=1
            count = max(r-l,count)
        return count