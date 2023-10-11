class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / mid)

            if time > h:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1
        return res