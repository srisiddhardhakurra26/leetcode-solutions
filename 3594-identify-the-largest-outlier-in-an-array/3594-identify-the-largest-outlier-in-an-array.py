class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        total = 0
        for n in nums:
            total += n
        for n in range(len(nums) - 1, -1, -1):
            total -= nums[n]
            res = nums[n]
            if total / 2 in counter and not (total // 2 == res and counter[res] == 1):
                return res
            total += nums[n]
        return -1