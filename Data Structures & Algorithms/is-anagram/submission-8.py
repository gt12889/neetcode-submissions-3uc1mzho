class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        c2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            count[i]=count.get(i,0)+1
        
        for i in t:
            c2[i]=c2.get(i,0)+1

        if c2 == count:
            return True
        else:
            return False