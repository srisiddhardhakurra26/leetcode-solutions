class Solution:
    def reorganizeString(self, s: str) -> str:
        hm = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in hm.items()]
        prev = None
        heapq.heapify(maxHeap)
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, ch = heapq.heappop(maxHeap)
            res += ch
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, ch]
                
        return res