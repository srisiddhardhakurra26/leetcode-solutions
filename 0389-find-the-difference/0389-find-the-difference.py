class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmt, hms = {}, {}
        for i in t:
            hmt[i] = 1 + hmt.get(i, 0)
        for j in s:
            hms[j] = 1 + hms.get(j, 0)
        for i in t:
            if i not in hms or hmt[i] > hms[i]:
                return i