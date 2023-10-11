class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            l, r = abs(nums[left]), abs(nums[right])
            if abs(l > r):
                res[right - left] = nums[left] ** 2
                left += 1
            else:
                res[right - left] = nums[right] ** 2
                right -= 1
        return res