class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, rlen = "",0

        for i in range(len(s)):
            for j in range(i,len(s)):
                l,r = i,j
                while l<r and s[l] == s[r]:
                    l+=1
                    r-=1
                if l>= r and rlen <(j-i+1):
                    res=s[i:j + 1]
                    rlen = j-i+1
        return res 