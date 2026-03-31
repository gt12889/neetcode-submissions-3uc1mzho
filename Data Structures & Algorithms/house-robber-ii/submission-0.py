class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robaction(nums[1:]),self.robaction(nums[:-1]))
    def robaction(self,nums):
        rob1, rob2 = 0,0
        for i in nums:
            tmp = max(rob1+i,rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2