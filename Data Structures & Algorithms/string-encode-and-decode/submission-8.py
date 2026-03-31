class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for i in strs:
            code+=str(len(i)) + "#" + i
        return code

    def decode(self, s: str) -> List[str]:
        code = []
        i,j=0,0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            leng = int(s[i:j])
            code.append(s[j+1:j+leng+1])
            i=j+leng+1
        return code
            