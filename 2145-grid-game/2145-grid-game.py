class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        prefix1, prefix2 = grid[0].copy(), grid[1].copy()

        for i in range(1, cols):
            prefix1[i] += prefix1[i - 1]
            prefix2[i] += prefix2[i - 1]
        
        res = float("inf")
        for i in range(cols):
            top = prefix1[-1] - prefix1[i]
            bottom = prefix2[i - 1] if i > 0 else 0
            second = max(top, bottom)
            res = min(res, second)
        return res