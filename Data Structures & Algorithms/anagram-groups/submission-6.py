class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        key = defaultdict(list)
        for i in strs:
            if str(sorted(i)) in key:
                key[str(sorted(i))].append(i)
            else:
                key[str(sorted(i))] = [i]

        return list(key.values())