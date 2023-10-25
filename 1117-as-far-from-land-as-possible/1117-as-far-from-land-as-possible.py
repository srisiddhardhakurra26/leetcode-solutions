class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        res = -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = dr + r, dc + c
                    if newR < 0 or newC < 0 or newR == rows or newC == cols or grid[newR][newC] == 1:
                        continue
                    grid[newR][newC] = 1 
                    q.append([newR, newC])            
            res += 1
        return res if res else -1
            
        
