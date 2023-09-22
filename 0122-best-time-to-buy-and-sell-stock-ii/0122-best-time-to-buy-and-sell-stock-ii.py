class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        ans = 0
        for i in range(len(prices) - 1):
            res.append(prices[i + 1] - prices[i])
        for j in res:
            if j > 0:
                ans += j
        return ans