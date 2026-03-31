class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for i in strs:
            s+=str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        ans = []
        length = 0
        i = 0
        j=0
        while j<len(s):
            while s[j] != "#":
                j+=1
                continue
            else:
                length = int(s[i:j])
                ans.append(s[j+1:j+1+length])
                j = j+1+length
            i = j
        return ans