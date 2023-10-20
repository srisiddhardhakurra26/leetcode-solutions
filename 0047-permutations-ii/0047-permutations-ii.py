class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(subres, remaining_nums):
            if not remaining_nums:
                res.append(subres.copy())
                return

            for i in range(len(remaining_nums)):
                if i > 0 and remaining_nums[i] == remaining_nums[i - 1]:
                    continue
                subres.append(remaining_nums[i])
                dfs(subres, remaining_nums[:i] + remaining_nums[i+1:])
                subres.pop()

        dfs([], nums)
        return res