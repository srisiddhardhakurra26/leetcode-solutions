class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        least = prices[0]
        for p in prices:
            least = min(least, p)
            res = max(res, p - least)
        return res