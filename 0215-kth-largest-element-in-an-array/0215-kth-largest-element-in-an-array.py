class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minh = []
        for n in nums:
            heapq.heappush(minh, n)
            if len(minh) > k:
                heapq.heappop(minh)
        return minh[0]
        