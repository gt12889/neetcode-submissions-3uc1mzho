class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        i=n
        while i:
            count+= i%2
            i = i>>1
        return count