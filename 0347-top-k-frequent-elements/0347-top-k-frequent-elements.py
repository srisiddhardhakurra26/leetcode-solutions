class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        for n, v in hm.items():
            freq[v].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res