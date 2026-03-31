class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not s[l].isalnum(): #cannot use if statemnt while will keep skipping until a valid char is found fpor edge cases where tehre are multiple non-alnum 
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True