class Solution:
    def minSwaps(self, s: str) -> int:
        count, maxcount = 0, 0
        for c in s:
            if c == "[":
                count -= 1
            else:
                count += 1
            maxcount = max(count, maxcount)
        return ((maxcount + 1) // 2)