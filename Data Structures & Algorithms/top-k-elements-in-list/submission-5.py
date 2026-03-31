class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        ans = []
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        bucket = [[] for i in range(len(nums)+1)]
        for n,c in freq.items():
            bucket[c].append(n)

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) ==k:
                    return ans