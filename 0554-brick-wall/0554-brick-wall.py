class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hm = {}
        for i in wall:
            leftsum = 0
            for j in i[:-1]:
                leftsum += j
                hm[leftsum] = 1 + hm.get(leftsum, 0)
        
        max_count = 0
        for key, value in hm.items():
            max_count = max(max_count, value)
        
        size = len(wall)
        return size - max_count