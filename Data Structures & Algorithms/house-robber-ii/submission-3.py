class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums: List[int]):
        rob1,rob2 = 0,0
        for i in nums:
            tmp = max(rob1+i,rob2)
            rob1 = rob2
            rob2=tmp
        return rob2