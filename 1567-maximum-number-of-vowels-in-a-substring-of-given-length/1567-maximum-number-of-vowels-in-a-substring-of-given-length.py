class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, count, res = 0, 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            if r - l + 1 > k:
                count -= 1 if s[l] in vowels else 0
                l += 1
            res = max(res, count)
        return res