class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(subres, remaining_nums):
            if not remaining_nums:
                res.append(subres)
                return

            for i in range(len(remaining_nums)):
                if i > 0 and remaining_nums[i] == remaining_nums[i - 1]:
                    continue
                dfs(subres + [remaining_nums[i]], remaining_nums[:i] + remaining_nums[i+1:])

        dfs([], nums)
        return res
