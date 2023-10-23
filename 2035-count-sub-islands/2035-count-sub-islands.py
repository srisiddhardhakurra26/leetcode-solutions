class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid2[r][c] == 0:
                return True

            if grid1[r][c] == 0:
                return False

            grid2[r][c] = 0
            return dfs(r+1, c) & dfs(r-1, c) & dfs(r, c+1) & dfs(r, c-1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        res += 1
        return res
