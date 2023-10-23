class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHigh):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or heights[r][c] < prevHigh:
                return

            visit.add((r, c))
            prevHigh = heights[r][c]
            dfs(r + 1, c, visit, prevHigh)
            dfs(r - 1, c, visit, prevHigh)
            dfs(r, c + 1, visit, prevHigh)
            dfs(r, c - 1, visit, prevHigh)
        
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols - 1, atlantic, 0)
        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows - 1, c, atlantic, 0)
        return list(pacific & atlantic)

        