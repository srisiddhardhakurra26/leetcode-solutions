class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        freq2 = [[] for n in range(len(nums) + 1)]
        for key, values in freq.items():
            freq2[values].append(key)
        for i in range(len(freq2) - 1, -1, -1):
            for val in freq2[i]:
                res.append(val)
                if len(res) == k:
                    return res