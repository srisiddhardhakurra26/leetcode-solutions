class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            tempstr = ","
            for n in freq:
                tempstr += str(n)
                tempstr += ','
            if tempstr not in res:
                res[tempstr] = []
            res[tempstr].append(s)
        return list(res.values())