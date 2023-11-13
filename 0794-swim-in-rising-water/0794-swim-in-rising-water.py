class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return height
            
            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc
                if (newRow < 0 or newCol < 0 or 
                    newRow == n or newCol == n or
                    (newRow, newCol) in visit):
                    continue
                visit.add((newRow, newCol))
                heapq.heappush(minHeap, [max(height, grid[newRow][newCol]), newRow, newCol])
            