class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, subres = [], []
        
        def dfs(i, curSum):
            if curSum == target:
                res.append(subres.copy())
                return 
            if curSum > target or i >= len(candidates):
                return

            curSum += candidates[i]
            subres.append(candidates[i])
            dfs(i, curSum)

            subres.pop()
            curSum -= candidates[i]
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res