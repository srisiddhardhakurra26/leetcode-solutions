class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}

        for i, j in rectangles:
            count[i / j] = 1 + count.get(i / j, 0)

        res = 0
        for i in count.values():
            if i > 1:
                res += (i * (i - 1)) // 2
        return res