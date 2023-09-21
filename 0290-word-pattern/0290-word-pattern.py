class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()

        if len(word) != len(pattern):
            return False
        chartoword = {}
        wordtochar = {}

        for c, w in zip(pattern, word):
            if c in chartoword and chartoword[c] != w:
                return False
            if w in wordtochar and wordtochar[w] != c:
                return False
            chartoword[c] = w
            wordtochar[w] = c
        return True
