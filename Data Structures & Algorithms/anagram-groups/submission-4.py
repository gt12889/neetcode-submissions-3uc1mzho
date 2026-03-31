class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        ans = []
        for i in strs:
            key_sorted = "".join(sorted(i))
            seen[key_sorted].append(i)
        return list(seen.values())