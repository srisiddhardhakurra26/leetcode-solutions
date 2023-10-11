class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2
            if ((mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1])):
                return nums[mid]
 
            size = mid - 1 if nums[mid - 1] == nums[mid] else mid
            if size % 2:
                right = mid - 1
            else:
                left = mid + 1