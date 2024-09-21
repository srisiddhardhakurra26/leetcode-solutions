class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        while left <= right:
            if leftMax < rightMax:
                res += max(leftMax - height[left], 0)
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                res += max(rightMax - height[right], 0)
                rightMax = max(rightMax, height[right])
                right -= 1
        return res