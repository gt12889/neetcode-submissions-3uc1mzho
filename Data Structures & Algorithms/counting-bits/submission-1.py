class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for j in range(n+1):
            one = 0
            for i in range(32):
                if j & (1 << i):
                    one+=1
            ans.append(one)
        return ans