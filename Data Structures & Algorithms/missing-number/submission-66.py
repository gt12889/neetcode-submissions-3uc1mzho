class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # If you want to keep your logic, sort first and fix the range
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)  # missing number is n