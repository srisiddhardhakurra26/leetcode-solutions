class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            x1, y1 = x * x, y * y
            dist.append([x1 + y1, x, y])
        
        res = []
        heapq.heapify(dist)
        for i in range(k):
            d, x, y = heapq.heappop(dist)
            res.append([x, y])
        return res

