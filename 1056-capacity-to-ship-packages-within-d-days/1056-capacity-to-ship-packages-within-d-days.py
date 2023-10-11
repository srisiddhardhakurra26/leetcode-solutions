class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = l + (r-l)//2

            m, d = mid, 1
            for w in weights:
                if m - w < 0:
                    m = mid
                    d += 1
                m -= w
            
            if d > days:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res