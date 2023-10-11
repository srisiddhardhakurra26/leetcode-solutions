class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            coinSum = (mid * (mid + 1)) // 2
            if n < coinSum:
                right = mid - 1
            elif n > coinSum:
                left = mid + 1
            else:
                return mid
        return right
