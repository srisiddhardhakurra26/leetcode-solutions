class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        minHeap = [] #[end, number of passengers]

        curPass = 0
        for t in trips:
            Passengers, start, end = t
            heapq.heappush(minHeap, [end, Passengers])
            while minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            curPass += Passengers
            if curPass > capacity:
                return False
        return True