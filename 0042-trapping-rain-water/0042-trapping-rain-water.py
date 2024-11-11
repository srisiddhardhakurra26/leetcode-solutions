class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0
        while left <= right:
            if leftMax <= rightMax:
                val = min(leftMax, rightMax) - height[left]
                if val > 0:
                    res += val
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                val = min(leftMax, rightMax) - height[right]
                if val > 0:
                    res += val
                rightMax = max(rightMax, height[right])
                right -= 1
        return res