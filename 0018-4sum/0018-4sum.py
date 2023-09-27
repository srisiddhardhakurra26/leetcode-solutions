class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        total, subtotal = 0, 0
        total = 0
        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target and [nums[i], nums[j], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res