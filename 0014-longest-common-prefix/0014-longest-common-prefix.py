class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) == i or c != strs[j][i]:
                    return res
            res += c
        return res