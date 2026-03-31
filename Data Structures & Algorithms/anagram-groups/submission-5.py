class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lkp = {}
        ans = []
        for i,j in enumerate(strs):
            key = str(sorted(j))
            if key in lkp:
                lkp[key].append(j)
            else:
                lkp[key] = [j]
        return list(lkp.values())   
