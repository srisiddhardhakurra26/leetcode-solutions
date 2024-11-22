class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openp, closep, subres):
            if openp > n:
                return
            if closep > openp:
                return
            if openp == n and closep == n:
                res.append(subres[:])
                return
            backtrack(openp + 1, closep, subres + "(")
            backtrack(openp, closep + 1, subres + ")")
            return
        backtrack(0, 0, "")
        return res