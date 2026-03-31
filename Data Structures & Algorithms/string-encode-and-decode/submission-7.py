class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s += "".join(str(len(i))+"#"+i)
        return s
    def decode(self, s: str) -> List[str]: 
        i,j = 0, 0
        ans = []
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            leng = int(s[i:j])
            ans.append(s[j+1:j+leng+1])
            i=j+1+leng
        return ans


