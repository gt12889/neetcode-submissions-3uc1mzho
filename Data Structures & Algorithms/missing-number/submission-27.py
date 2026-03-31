class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for j in range(len(nums)):
            if nums[j] !=j:
                return j
        return len(nums)