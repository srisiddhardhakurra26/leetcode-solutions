class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh, time = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    continue
                fresh += grid[r][c]
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newC < 0 or newR == rows or newC == cols or grid[newR][newC] != 1:
                        continue
                    q.append([newR, newC])
                    grid[newR][newC] = 2
                    fresh -= 1
            time += 1
        return time if not fresh else -1

                