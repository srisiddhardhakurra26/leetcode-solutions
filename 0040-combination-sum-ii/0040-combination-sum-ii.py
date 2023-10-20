class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subres = [], []
        candidates.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(subres.copy())
                return
            if curSum > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                subres.append(candidates[j])
                dfs(j + 1, curSum + candidates[j])
                subres.pop()
        
        dfs(0, 0)
        return res
