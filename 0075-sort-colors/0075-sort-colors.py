class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = []
        heapq.heapify(nums)
        while nums:
            res.append(heapq.heappop(nums))
        nums[ : ] = res