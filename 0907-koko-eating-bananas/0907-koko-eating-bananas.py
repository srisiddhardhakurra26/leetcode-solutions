class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / m)
            if curr_hours > h:
                l = m+1
            else:
                r = m
        return l

