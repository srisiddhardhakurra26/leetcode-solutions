class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [0] * (len(nums) + 1)
        for n in nums:
            freq[n] += 1
        freq2 = [[] for n in range(len(nums) + 1)]
        for number, frequency in enumerate(freq):
            if frequency:
                freq2[frequency].append(number)
        for i in range(len(freq2) - 1, -1, -1):
            for val in freq2[i]:
                res.append(val)
                if len(res) == k:
                    return res