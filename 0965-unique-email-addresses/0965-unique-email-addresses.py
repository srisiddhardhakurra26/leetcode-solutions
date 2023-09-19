class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for s in emails:
            i, j = 0, 0
            st = ""
            while s[j]!= '@':
                j += 1
            while i != j and s[i] != '+':
                if s[i] != '.':
                    st += s[i]
                i += 1
            while j < len(s):
                st += s[j]
                j += 1
            res.add(st)
        return len(res)