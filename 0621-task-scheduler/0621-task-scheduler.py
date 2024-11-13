class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap, q, time = [], deque(), 0
        counter = Counter(tasks)
        for task, freq in counter.items():
            maxHeap.append(-freq)
        heapq.heapify(maxHeap)
        while maxHeap or q:
            time += 1
            while q and q[0][0] <= time:
                heapq.heappush(maxHeap, q.pop()[1])
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 < 0:
                    q.append([time + n + 1, freq + 1])
        return time