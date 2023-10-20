class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subres = [], []

        def dfs(i):
            if i == len(nums):
                res.append(subres.copy())
                return
            
            subres.append(nums[i])
            dfs(i + 1)
            subres.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
            