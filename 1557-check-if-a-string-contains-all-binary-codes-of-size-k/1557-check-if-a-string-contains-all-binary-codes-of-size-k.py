class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        size = 2 ** k
        unique = set()
        for l in range(len(s) - k + 1):
            unique.add(s[l : l + k])
        if len(unique) == size:
            return True
        else:
            return False
            