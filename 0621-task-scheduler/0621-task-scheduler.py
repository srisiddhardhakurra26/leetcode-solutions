class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxheap = [-v for v in count.values()]
        heapq.heapify(maxheap)
        q = collections.deque()

        while maxheap or q:
            time += 1
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time