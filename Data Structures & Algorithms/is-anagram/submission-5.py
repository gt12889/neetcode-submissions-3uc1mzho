class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        count = {}
        for c in s:
            count[c] = count.get(c,0)+1
        for c in t:
            if c not in count:
                return False
            count[c] -=1 #were decermenting here so each loop will still need to subtrack other counts
            if count[c] < 0: #if its less than 0 it will be falase, line 8 checks if there is too many c in s
                return False
        return True
        