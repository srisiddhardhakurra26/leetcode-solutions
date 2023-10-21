class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, curStr = [], ""
        hm = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        def dfs(i):
            nonlocal curStr
            if len(digits) == len(curStr):
                res.append(curStr[:])
                return

            for j in hm[digits[i]]:
                curStr += j
                dfs(i + 1)
                curStr = curStr[:-1]


        dfs(0)
        if digits:
            return res