class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrice = prices.copy()
            for src, dest, price in flights:
               
                if prices[src] + price < tmpPrice[dest]:
                    tmpPrice[dest] = prices[src] + price
            prices = tmpPrice
        return -1 if prices[dst] == float("inf") else prices[dst]