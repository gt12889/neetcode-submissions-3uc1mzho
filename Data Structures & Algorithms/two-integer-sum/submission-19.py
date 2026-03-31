class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            need = target - n
            if need in map:
                return [map[need],i]
            map[n] = i
        return []