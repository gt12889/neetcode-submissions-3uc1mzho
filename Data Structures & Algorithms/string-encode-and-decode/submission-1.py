class Solution:

    def encode(self, strs: List[str]) -> str:
        total_word = ""
        for i in strs:
            total_word += str(len(i)) +"#" + i
        return total_word


    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        j = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i= j+1+length
        return ans
        