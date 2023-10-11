class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            mid = left + (right - left)//2
            squaredMid = mid * mid
            if squaredMid > x:
                right = mid - 1
            elif squaredMid < x:
                left = mid + 1
            else:
                return mid
        return right