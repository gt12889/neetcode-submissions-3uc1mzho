class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort for optimal solution but it the obvious way wont work since the data set is unbounded, if it was bounded it would work
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res #we know it will be equal to k at some point O(n)

