class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        side = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if side == 0:
                    side = 1
                elif side == -1:
                    return False
            elif nums[i] < nums[i - 1]:
                if side == 0:
                    side = -1
                elif side == 1:
                    return False
        return True