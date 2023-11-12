class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        res = 0
        minHeap = [[0, k]]
        visit = set()
        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res = max(res, dist)
            visit.add(node)
            for nei, neiDist in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [dist + neiDist, nei])
        return res if len(visit) == n else -1