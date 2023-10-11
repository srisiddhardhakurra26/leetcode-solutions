class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        res = [0] * len(people)
        start = [f[0] for f in flowers]
        heapq.heapify(start)
        end = [f[1] for f in flowers]
        heapq.heapify(end)
        count = 0

        for p, i in sorted(people):
            while start and start[0] <= p:
                count += 1
                heapq.heappop(start)
            while end and end[0] < p:
                count -= 1
                heapq.heappop(end)
            res[i] = count
        return res
