class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 1
        mini = 1

        ans = nums[0]
        for i in range(0,len(nums)):
            tmp = maxi*nums[i]
            maxi=max(nums[i],tmp,mini*nums[i])            
            mini=min(mini*nums[i],nums[i],tmp)
            ans = max(maxi,ans)
        return ans