class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        if len(nums) == 1:
            return nums

        for i in range(k):
            bigval, bigkey = 0, 0
            for key, value in hm.items():
                if value > bigval:
                    bigval, bigkey = value, key
            res.append(bigkey)
            hm.pop(bigkey)
        
        return res