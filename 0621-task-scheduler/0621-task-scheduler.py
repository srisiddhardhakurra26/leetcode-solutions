class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        maxHeap = []
        counter = Counter(tasks)
        for key, value in counter.items():
            maxHeap.append(-value)
        heapq.heapify(maxHeap)
        q = deque()
        while maxHeap or q:
            time += 1
            while q and q[0][0] <= time:
                heapq.heappush(maxHeap, q.pop()[1])
            if maxHeap:
                task = heapq.heappop(maxHeap)
                if task + 1 < 0:
                    q.append([time + n + 1, task + 1])
        return time