class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        curr =0
        maxi = nums[0]

        for i in range(0,len(nums)):
            maxi = max(maxi,curr+nums[i])
            curr+=nums[i]
            if curr < 0:
                curr=0
        return maxi
