class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        return freq == [0] * 26