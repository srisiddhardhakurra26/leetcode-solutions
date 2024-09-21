class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = [0] * 26
        check_t = [0] * 26
        for c in s:
            check_s[ord(c) - ord('a')] += 1
        for c in t:
            check_t[ord(c) - ord('a')] += 1
        for i in range(26):
            if check_s[i] != check_t[i]:
                return False
        return True