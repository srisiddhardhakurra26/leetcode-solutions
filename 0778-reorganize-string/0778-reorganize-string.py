class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = []
        if max(counter.values()) > (len(s) + 1) // 2:
            return ""
        #start with highest frequency alphabet
        for key, value in counter.items():
            maxHeap.append([-value, key])
        heapq.heapify(maxHeap)
        prev = None
        res = ""
        while maxHeap or prev:
            freq, letter = heapq.heappop(maxHeap)
            res += letter
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if freq + 1 != 0:
                prev = [freq + 1, letter]
        return res