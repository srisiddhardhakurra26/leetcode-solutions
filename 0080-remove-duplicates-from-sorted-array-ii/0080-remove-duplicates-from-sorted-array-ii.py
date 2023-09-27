class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        count = 1
        for fast in range(1, len(nums)):
            if nums[slow] == nums[fast] and count < 2:
                slow += 1
                nums[slow] = nums[fast]
                count += 1
            elif nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
                count = 1
        return slow + 1