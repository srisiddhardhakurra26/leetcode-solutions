class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxcount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxcount else res
            maxcount = max(maxcount, count[n])
        return res
