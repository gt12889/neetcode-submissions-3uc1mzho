class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        
        key = {}
        l,r = 0,0
        mlength = float("inf")

        for i in t:
            key[i] = 1+ key.get(i,0)

        while r < len(s):
            if s[r] in key:
                key[s[r]]-=1
            while all(value <= 0 for value in key.values()):
                if mlength > (r-l+1):
                    mlength = (r-l+1)
                    ans=s[l:r+1]
                if s[l] in key:
                    key[s[l]]+=1
                l+=1
            r+=1
        return ans
