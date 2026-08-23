class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return False
        ans = nums[0]
        cur = 0

        for n in nums:
            if cur <0:
                cur =0
            cur+=n
            ans = max(ans,cur)
        return ans