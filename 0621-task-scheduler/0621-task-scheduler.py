class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        res = 0
        counter = Counter(tasks)
        for value in counter.values():
            maxHeap.append(-value)
        heapq.heapify(maxHeap)
        q = deque([])
        while maxHeap or q:
            res += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
            if freq + 1 < 0:
                freq += 1
                q.append([n + res, freq])
            while q and q[0][0] <= res:
                _, freq = q.popleft()
                heapq.heappush(maxHeap, freq)
        return res