class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        far = nums[0]
        n = len(nums)-1
        i = 0
        while i <= len(nums)-1:
            if far < i:
                return False
            if far > n:
                return True
            far = max(far,i+nums[i])
            i+=1
        return True