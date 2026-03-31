class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1
        l = 0
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum(): #not .isalnum()
                r-=1
            if l < r and s[l].lower()!=s[r].lower(): #l < r needed for safety check, else it would compare pointers cross
                return False
            l+=1
            r-=1
        return True
