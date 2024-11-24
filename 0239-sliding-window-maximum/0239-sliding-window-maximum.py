class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        for r in range(k, len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r - left + 1 > k:
                left += 1
            if q and q[0] < left:
                q.popleft()
            res.append(nums[q[0]])
        return res