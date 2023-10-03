class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = {}
        res = 0

        for i in nums:
            hm[i] = 1 + hm.get(i, 0)
        
        for i in hm.values():
            if i > 1:
                res += (i * (i - 1)) // 2
        return res
