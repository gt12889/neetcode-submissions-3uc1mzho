class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest =0
        dup = set(nums)

        for n in nums:
            if n-1 not in dup:
                length = 1
                while n+1 in dup:
                    length+=1
                    n+=1
                longest = max(length,longest)
        return longest