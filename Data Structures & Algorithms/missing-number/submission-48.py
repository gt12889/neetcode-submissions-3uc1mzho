class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[len(nums)-1]
        for i in range(n):
            if i != nums[i]:
                return i
        return n+1
