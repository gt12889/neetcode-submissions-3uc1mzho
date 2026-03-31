class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans,i = 0,0
        nums.sort()
        if nums[0] != 0:
            return 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]+1:
                i+=1
            else:
                return nums[i]+1
        return nums[i]+1