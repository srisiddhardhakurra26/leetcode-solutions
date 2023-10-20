class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, subres = [], []

        def dfs():
            if len(subres) == len(nums):
                res.append(subres.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in subres:
                    subres.append(nums[i])
                    dfs()
                    subres.pop()

        dfs()
        return res