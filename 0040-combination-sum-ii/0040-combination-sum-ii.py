class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res, subres = [], []
        nums.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(subres.copy())
                return
            
            if i >= len(nums) or curSum > target:
                return
            
            curSum += nums[i]
            subres.append(nums[i])
            dfs(i + 1, curSum)
            subres.pop()
            curSum -= nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res