class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far =0 
        i = 0
        if len(nums)==0:
            return True
        while i<=len(nums)-1:
            if far < i:
                return False
            if far >= len(nums)-1:
                return True
            far = max(far,i+nums[i])
            i+=1
        return False
