class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i #i will be the number before teh #, resdetting aft4r each string
            while s[j] != "#":
                j+=1
            length=int(s[i:j]) # how manby characters to read to do the decoding
            ans.append(s[j+1:j+1+length]) #staarting afer the # to #+length
            i=j+1+length # resetting i to the end of the word that was just added
        return ans

            