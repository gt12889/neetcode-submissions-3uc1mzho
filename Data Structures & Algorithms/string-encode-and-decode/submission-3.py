class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ''
        for s in strs:
            new += str(len(s))+"#"+s
        return new

    def decode(self, s: str) -> List[str]:
        word = []
        j=0
        while j < len(s):
            i=j
            while s[i] != "#":
                i+=1
            length = int(s[j:i])
            word.append(s[i+1:i+1+length])
            j = i + 1 + length
        return word