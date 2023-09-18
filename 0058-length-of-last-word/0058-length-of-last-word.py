class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len = 0
        word = False
        for ch in s[::-1]:
            if ch != " ":
                len += 1
                word = True
            elif word:
                return len
        
        return len