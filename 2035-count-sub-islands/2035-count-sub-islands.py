class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid2[r][c] == 0:
                return True

            if grid1[r][c] == 0:
                return False

            grid2[r][c] = 0  # Mark cell as visited in grid2
            is_sub_island = True  # Initialize as True

            # Recursively check adjacent cells
            is_sub_island &= dfs(r + 1, c)
            is_sub_island &= dfs(r - 1, c)
            is_sub_island &= dfs(r, c + 1)
            is_sub_island &= dfs(r, c - 1)

            return is_sub_island

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        res += 1
        return res
