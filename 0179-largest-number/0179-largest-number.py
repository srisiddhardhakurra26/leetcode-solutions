class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]
        for i in nums:
            res += str(i)
        return "0" if int(res) == 0 else res