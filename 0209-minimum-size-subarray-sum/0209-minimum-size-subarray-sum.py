class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, res, total = 0, len(nums) + 1, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res <= len(nums) else 0