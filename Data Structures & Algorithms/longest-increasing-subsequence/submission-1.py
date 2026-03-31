class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        maxi = 0
        if not nums:
            return 0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    lis[i] = max(lis[i],lis[j]+1)
        return max(lis)