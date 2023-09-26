class Solution:
    def partitionString(self, s: str) -> int:
        newstr = ""
        res = 0
        for i in s:
            if i in newstr:
                newstr = ""
                res += 1
            newstr += i
        return res + 1