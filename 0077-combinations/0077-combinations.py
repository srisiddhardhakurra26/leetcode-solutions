class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, subres = [], []

        def dfs(i):
            if len(subres) == k:
                res.append(subres.copy())
                return
            if i > n:
                return 
            
            subres.append(i)
            dfs(i + 1)
            subres.pop()
            dfs(i + 1)

        dfs(1)
        return res