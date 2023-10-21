class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, subres = [], ""
        if len(s) > 12 or len(s) < 4:
            return res
        
        def dfs(i, dots, subres):
            if dots == 4 and i == len(s):
                res.append(subres[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    dfs(j + 1, dots + 1, subres + s[i:j+1] + ".")

        dfs(0 , 0, "")
        return res