class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        if len(nums) == 1:
            return [nums[0]]
        for i in range(len(nums)):
            curr = [num for num in nums]
            curr.remove(nums[i])
            prod = 1
            for j in curr:
                prod *= j
            ans.append(prod)
        return ans