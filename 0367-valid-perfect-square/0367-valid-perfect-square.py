class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + (right - left)//2
            squaredMid = (left + (right - left)//2) ** 2
            if squaredMid > num:
                right = mid - 1
            elif squaredMid < num:
                left = mid + 1
            else:
                return True
        return False