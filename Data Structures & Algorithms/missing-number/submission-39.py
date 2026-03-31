class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n + 1):          # check every number from 0..n
            found = False

            for j in range(n):          # scan entire array
                if nums[j] == i:
                    found = True
                    break

            if not found:
                return i
