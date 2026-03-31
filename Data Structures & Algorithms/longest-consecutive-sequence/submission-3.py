class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            consec_set = set(nums)
            longest = 0
            for num in consec_set:
                if num-1 not in consec_set:
                    length=1
                    current = num
                    while current +1 in consec_set:
                        length+=1
                        current+=1
                    longest = max(length,longest)
            return longest