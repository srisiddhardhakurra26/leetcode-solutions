class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hm = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        def dfs(i, curStr):
            if len(digits) == len(curStr):
                res.append(curStr[:])
                return

            for j in hm[digits[i]]:
                dfs(i + 1, curStr + j)


        if digits: dfs(0, "")
        return res 