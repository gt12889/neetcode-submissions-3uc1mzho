class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        for i in range(len(nums)):
            curr=nums[i]
            maxi = max(curr,maxi)
            for j in range(i+1,len(nums)):
                curr *= nums[j]
                maxi=max(curr,maxi)
        return maxi