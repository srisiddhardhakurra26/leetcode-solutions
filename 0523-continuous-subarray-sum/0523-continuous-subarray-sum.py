class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm = { 0:-1 }
        total = 0

        for i, v in enumerate(nums):
            total += v
            r = total % k
            if r not in hm:
                hm[r] = i
            elif i - hm[r] > 1:
                return True