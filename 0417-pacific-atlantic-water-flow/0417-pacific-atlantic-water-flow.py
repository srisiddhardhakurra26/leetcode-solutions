class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])
        
        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))
            prevHeight = heights[r][c]
            dfs(r + 1, c, visit, prevHeight)
            dfs(r - 1, c, visit, prevHeight)
            dfs(r, c + 1, visit, prevHeight)
            dfs(r, c - 1, visit, prevHeight)


        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        return list(atl & pac)